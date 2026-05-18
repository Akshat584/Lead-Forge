from pydantic import BaseModel, ConfigDict
from typing import Optional, Dict, Any
from uuid import UUID
from datetime import datetime

class AIAnalysisBase(BaseModel):
    score: Optional[int] = None
    confidence: Optional[float] = None
    reasoning: Optional[str] = None
    recommended_action: Optional[str] = None
    sentiment: Optional[str] = None
    generated_email: Optional[str] = None
    model_used: Optional[str] = None
    tokens_used: Optional[int] = None
    metadata_: Optional[Dict[str, Any]] = None

class AIAnalysisCreate(AIAnalysisBase):
    lead_id: UUID

class AIAnalysisResponse(AIAnalysisBase):
    id: UUID
    lead_id: UUID
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
