from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.mixins import UUIDPrimaryKeyMixin, TimestampMixin

class ActivityLog(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "activity_logs"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), index=True, nullable=False)

    action_type = Column(String, nullable=False)
    metadata_ = Column("metadata", JSONB, default=dict)
    ip_address = Column(String)

    user = relationship("User", back_populates="activity_logs")
