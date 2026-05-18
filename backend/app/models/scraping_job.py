from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.mixins import UUIDPrimaryKeyMixin, TimestampMixin

class ScrapingJob(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "scraping_jobs"

    campaign_id = Column(UUID(as_uuid=True), ForeignKey("campaigns.id"), index=True, nullable=False)

    query = Column(String, nullable=False)
    status = Column(String, default="PENDING", index=True)

    total_results = Column(Integer, default=0)
    processed_results = Column(Integer, default=0)
    failed_results = Column(Integer, default=0)

    started_at = Column(DateTime(timezone=True))
    completed_at = Column(DateTime(timezone=True))

    error_message = Column(String)

    campaign = relationship("Campaign", back_populates="scraping_jobs")
