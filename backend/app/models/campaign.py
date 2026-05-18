from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.mixins import UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin

class Campaign(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "campaigns"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), index=True, nullable=False)

    name = Column(String, nullable=False)
    description = Column(String)

    status = Column(String, default="DRAFT", index=True)

    target_industry = Column(String)
    target_location = Column(String)
    target_company_size = Column(String)

    outreach_channel = Column(String, default="EMAIL")

    scraping_query = Column(String)
    ai_prompt = Column(String)

    total_leads = Column(Integer, default=0)
    qualified_leads = Column(Integer, default=0)
    contacted_count = Column(Integer, default=0)
    reply_count = Column(Integer, default=0)

    metadata_ = Column("metadata", JSONB, default=dict)

    user = relationship("User", back_populates="campaigns")
    leads = relationship("Lead", back_populates="campaign", cascade="all, delete-orphan")
    outreach_logs = relationship("OutreachLog", back_populates="campaign", cascade="all, delete-orphan")
    scraping_jobs = relationship("ScrapingJob", back_populates="campaign", cascade="all, delete-orphan")
