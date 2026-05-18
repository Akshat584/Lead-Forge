from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.mixins import UUIDPrimaryKeyMixin, TimestampMixin

class OutreachLog(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "outreach_logs"

    lead_id = Column(UUID(as_uuid=True), ForeignKey("leads.id"), index=True, nullable=False)
    campaign_id = Column(UUID(as_uuid=True), ForeignKey("campaigns.id"), index=True, nullable=False)

    channel = Column(String, nullable=False)
    subject = Column(String)
    message = Column(String, nullable=False)

    delivery_status = Column(String)
    reply_detected = Column(Boolean, default=False, index=True)

    sent_at = Column(DateTime(timezone=True), index=True)
    opened_at = Column(DateTime(timezone=True))
    replied_at = Column(DateTime(timezone=True))

    lead = relationship("Lead", back_populates="outreach_logs")
    campaign = relationship("Campaign", back_populates="outreach_logs")
