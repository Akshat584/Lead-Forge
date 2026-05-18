from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, Dict, Any
from uuid import UUID
from datetime import datetime
from app.core.enums import LeadStatus

class LeadBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    full_name: Optional[str] = None
    email: EmailStr
    phone: Optional[str] = None
    job_title: Optional[str] = None
    company_name: Optional[str] = None
    company_website: Optional[str] = None
    linkedin_url: Optional[str] = None
    industry: Optional[str] = None
    company_size: Optional[str] = None
    location: Optional[str] = None
    source: Optional[str] = None
    source_url: Optional[str] = None

class LeadCreate(LeadBase):
    campaign_id: UUID

class LeadUpdate(BaseModel):
    ai_score: Optional[int] = None
    status: Optional[LeadStatus] = None
    ai_summary: Optional[str] = None
    personalization_data: Optional[Dict[str, Any]] = None
    verification_status: Optional[str] = None
    enrichment_status: Optional[str] = None
    notes: Optional[str] = None

class LeadResponse(LeadBase):
    id: UUID
    campaign_id: UUID
    ai_score: Optional[int] = None
    status: Optional[LeadStatus] = None
    ai_summary: Optional[str] = None
    personalization_data: Optional[Dict[str, Any]] = None
    verification_status: Optional[str] = None
    enrichment_status: Optional[str] = None
    notes: Optional[str] = None
    last_contacted_at: Optional[datetime] = None
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
