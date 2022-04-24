from http import client
from typing import List

from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine
from config import Settings, get_settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/ping")
async def ping(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }

    
@app.post("/client/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    db_client = crud.get_client_by_cnpj(db, cnpj=client.cnpj)
    if db_client:
        raise HTTPException(status_code=400, detail="CNPJ already registered")
    return crud.create_client(db=db, client=client)


@app.get("/client/", response_model=List[schemas.Client])
def read_client(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clients = crud.get_clients(db, skip=skip, limit=limit)
    return clients


@app.get("/clients/{client_id}", response_model=schemas.Client)
def read_client(client_id: int, db: Session = Depends(get_db)):
    db_client = crud.get_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client


@app.post("/client/{client_id}/licenses/", response_model=schemas.License)
def create_license_for_client(
    client_id: int, license: schemas.LicenseCreate, db: Session = Depends(get_db)
):
    return crud.create_client_license(db=db, license=license, client_id=client_id)


@app.get("/licenses/", response_model=List[schemas.License])
def read_licenses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    licenses = crud.get_licenses(db, skip=skip, limit=limit)
    return licenses
