from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint, DateTime
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.mixins import UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin

class Lead(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "leads"
    
    campaign_id = Column(UUID(as_uuid=True), ForeignKey("campaigns.id"), index=True, nullable=False)

    first_name = Column(String)
    last_name = Column(String)
    full_name = Column(String)

    email = Column(String, index=True)
    phone = Column(String)
    job_title = Column(String)

    company_name = Column(String, index=True)
    company_website = Column(String)
    linkedin_url = Column(String)

    industry = Column(String)
    company_size = Column(String)
    location = Column(String)

    source = Column(String)
    source_url = Column(String)

    ai_score = Column(Integer, index=True)
    status = Column(String, index=True)

    ai_summary = Column(String)
    personalization_data = Column(JSONB, default=dict)

    verification_status = Column(String)
    enrichment_status = Column(String)

    notes = Column(String)
    last_contacted_at = Column(DateTime(timezone=True))

    __table_args__ = (UniqueConstraint("campaign_id", "email", name="uq_campaign_email"),)

    campaign = relationship("Campaign", back_populates="leads")
    ai_analyses = relationship("AIAnalysis", back_populates="lead", cascade="all, delete-orphan")
    outreach_logs = relationship("OutreachLog", back_populates="lead", cascade="all, delete-orphan")
