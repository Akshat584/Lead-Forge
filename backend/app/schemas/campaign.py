from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime
from app.core.enums import CampaignStatus, OutreachChannel

class CampaignBase(BaseModel):
    name: str
    description: Optional[str] = None
    target_industry: Optional[str] = None
    target_location: Optional[str] = None
    target_company_size: Optional[str] = None
    outreach_channel: OutreachChannel = OutreachChannel.EMAIL
    scraping_query: Optional[str] = None
    ai_prompt: Optional[str] = None

class CampaignCreate(CampaignBase):
    pass

class CampaignUpdate(BaseModel):
    name: Optional[str] = None
    status: Optional[CampaignStatus] = None
    description: Optional[str] = None

class CampaignResponse(CampaignBase):
    id: UUID
    user_id: UUID
    status: CampaignStatus
    total_leads: int
    qualified_leads: int
    contacted_count: int
    reply_count: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
