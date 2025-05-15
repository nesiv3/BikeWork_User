import os
from typing import List
from dotenv import load_dotenv
from sqlalchemy import Column, String, Date, DateTime, Text, ForeignKey, Boolean, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime



# Cargar variables de ent
load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class UserORM(Base):
    __tablename__ = "user"
    id = Column(String(36), primary_key=True)
    full_name = Column(String(150))
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    profile : Mapped["UserProfileORM"] = relationship(lazy="selectin", uselist=False)
    roles: Mapped[List["UserRoleORM"]] = relationship(lazy="selectin")

class UserProfileORM(Base):
    __tablename__ = "user_profile"
    user_id : Mapped[String] = mapped_column(ForeignKey("user.id"),primary_key=True)
    email = Column(String(255), nullable=False)
    birthdate = Column(Date)
    gender = Column(String(20))
    address_line1 = Column(Text)
    address_line2 = Column(Text)
    city = Column(String(100), nullable=False)
    country = Column(String(100))
    emergency_contact_name = Column(String(150))
    emergency_contact_phone = Column(String(20))
    avatar_url = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    phone_number = Column(String(20), nullable=False)
    

class UserRoleORM(Base):
    __tablename__ = "user_role"
    user_id  : Mapped[String] = Column(String(36), ForeignKey("user.id", ondelete="CASCADE"), primary_key=True)
    role_catalog_id = Column(String(10), primary_key=True)
    assigned_at = Column(DateTime, default=datetime.utcnow)
   