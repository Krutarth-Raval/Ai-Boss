from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

# --- Research Schemas ---
class MarketResearchSchema(BaseModel):
    industry: str
    market_size: str
    growth_rate: str
    top_companies: List[str]
    opportunities: List[str]
    risks: List[str]

# --- Sales Schemas ---
class LeadSchema(BaseModel):
    company_name: str
    industry: str
    location: str
    website: str
    contact_email: str
    lead_score: int
    reason_for_targeting: str

class LeadListSchema(BaseModel):
    leads: List[LeadSchema]

class SalesStrategySchema(BaseModel):
    outreach_channels: List[str]
    pitch_summary: str
    target_leads: List[LeadSchema]
    follow_up_plan: str

# --- Marketing Schemas ---
class MarketingPlanSchema(BaseModel):
    target_audience: str
    channels: List[str]
    content_strategy: List[str]
    budget_estimate: str
    expected_roi: str

# --- Finance Schemas ---
class FinanceReportSchema(BaseModel):
    estimated_revenue: str
    projected_costs: str
    profit_margin: str
    financial_risks: List[str]

# --- Operations Schemas ---
class OperationsPlanSchema(BaseModel):
    workflow_steps: List[str]
    efficiency_improvements: List[str]
    resource_allocation: Dict[str, str]

# --- Recruitment Schemas ---
class HiringCandidateSchema(BaseModel):
    name: str
    skills: List[str]
    experience_years: int
    expected_salary: str
    fit_score: int

# --- Strategy Schemas ---
class BusinessStrategySchema(BaseModel):
    strategic_objective: str
    key_results: List[str]
    timeline: str
    risk_mitigation: List[str]

# --- Analytics Schemas ---
class PerformanceInsightsSchema(BaseModel):
    metrics: Dict[str, Any]
    growth_trends: List[str]
    recommendations: List[str]
