from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.mixins import UUIDPrimaryKeyMixin, TimestampMixin

class AIAnalysis(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "ai_analyses"

    lead_id = Column(UUID(as_uuid=True), ForeignKey("leads.id"), index=True, nullable=False)

    score = Column(Integer)
    confidence = Column(Float)

    reasoning = Column(String)
    recommended_action = Column(String)
    sentiment = Column(String)
    generated_email = Column(String)

    model_used = Column(String)
    tokens_used = Column(Integer)

    metadata_ = Column("metadata", JSONB, default=dict)

    lead = relationship("Lead", back_populates="ai_analyses")
