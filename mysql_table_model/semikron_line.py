# pylint: skip-file
"""塞米控印刷线体表模型."""
from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base


BASE = declarative_base()


class PrintPaint(BASE):
    """刷绿色油漆设备."""

    __tablename__ = "print_paint"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    dcb_code = Column(String(50), nullable=True)  # dcb id
    dcb_code_index = Column(Integer, nullable=True)  # dcb id index
    vacuum_carrier_code = Column(String(50), nullable=True)  # 真空底座 id
    nozzle_code = Column(String(50), nullable=True)  # 吸嘴 id
    silk_code = Column(String(50), nullable=True)  # 丝网 id
    carrier_code = Column(String(50), nullable=True)  # 托盘 id
    paint_code = Column(String(50), nullable=True)  # 绿色油漆 id
    paint_batch_code = Column(String(50), nullable=True)  # 绿色油漆 batch id
    lot_code = Column(String(50), nullable=True)
    article_code = Column(String(50), nullable=True)
    updated_at = Column(DateTime, default=lambda: datetime.now(), onupdate=lambda: datetime.now())
    created_at = Column(DateTime, default=lambda: datetime.now())

    def as_dict(self):
        """获取字典形式的数据."""
        return {column.name: getattr(self, column.name) for column in self.__table__.columns.values()}


class PrintSolderPaste(BASE):
    """刷锡膏设备."""

    __tablename__ = "print_solder_paste"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    dcb_code = Column(String(50), nullable=True)  # dcb id
    dcb_code_index = Column(Integer, nullable=True)  # dcb id index
    vacuum_carrier_code = Column(String(50), nullable=True)  # 真空底座 id
    nozzle_code = Column(String(50), nullable=True)  # 吸嘴 id
    silk_code = Column(String(50), nullable=True)  # 丝网 id
    carrier_code = Column(String(50), nullable=True)  # 托盘 id
    solder_paste_code = Column(String(50), nullable=True)  # 锡膏 id
    solder_paste_batch_code = Column(String(50), nullable=True)  # 锡膏 batch id
    lot_code = Column(String(50), nullable=True)
    article_code = Column(String(50), nullable=True)
    updated_at = Column(DateTime, default=lambda: datetime.now(), onupdate=lambda: datetime.now())
    created_at = Column(DateTime, default=lambda: datetime.now())

    def as_dict(self):
        """获取字典形式的数据."""
        return {column.name: getattr(self, column.name) for column in self.__table__.columns.values()}


class MicroscopicInspection(BASE):
    """人工镜检台."""

    __tablename__ = "microscopic_inspection"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    dcb_code = Column(String(50), nullable=True)
    inspection_result = Column(Integer, nullable=True)
    lot_code = Column(String(50), nullable=True)
    article_code = Column(String(50), nullable=True)
    photo_path = Column(String(50), nullable=True)
    updated_at = Column(DateTime, default=lambda: datetime.now(), onupdate=lambda: datetime.now())
    created_at = Column(DateTime, default=lambda: datetime.now())

    def as_dict(self):
        """获取字典形式的数据."""
        return {column.name: getattr(self, column.name) for column in self.__table__.columns.values()}


class Cutting(BASE):
    """下料设备."""

    __tablename__ = "cutting"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    carrier_code = Column(String(50), nullable=True)
    magazine_code = Column(String(50), nullable=True)
    lot_code = Column(String(50), nullable=True)
    article_code = Column(String(50), nullable=True)
    updated_at = Column(DateTime, default=lambda: datetime.now(), onupdate=lambda: datetime.now())
    created_at = Column(DateTime, default=lambda: datetime.now())

    def as_dict(self):
        """获取字典形式的数据."""
        return {column.name: getattr(self, column.name) for column in self.__table__.columns.values()}
