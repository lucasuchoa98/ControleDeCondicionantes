from sqlalchemy.orm import Session

import models, schemas

def get_client(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()

def get_client_by_cnpj(db: Session, cnpj: str):
    return db.query(models.Client).filter(models.Client.cnpj== cnpj).first()

def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()


def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_license(db: Session, license_id: int):
    return db.query(models.License).filter(models.License.id == license_id).first()

def get_licenses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.License).offset(skip).limit(limit).all()

def create_client_license(db: Session, client: schemas.LicenseCreate, client_id: int):
    db_license = models.License(**client.dict(), client_id=client_id)
    db.add(db_license)
    db.commit()
    db.refresh(db_license)
    return db_license
