export type Role = 
  | 'college_inst' 
  | 'university' 
  | 'rb_officer' 
  | 'pgrc_officer' 
  | 'admin' 
  | 'ro_officer' 
  | 'senior_mgmt';

export type Priority = 'Urgent' | 'High' | 'Medium' | 'Low';

export type ComplaintStatus = 
  | 'Draft'
  | 'Verification Pending'
  | 'Submitted'
  | 'Under Review'
  | 'Under Process' // legacy compatibility
  | 'Pending'       // legacy compatibility
  | 'Additional Information Required'
  | 'Investigation'
  | 'Escalated'
  | 'Resolved'
  | 'Disposed'      // legacy compatibility
  | 'Transferred'   // legacy compatibility
  | 'Closed';

export type Bureau = 
  | 'Regulation Bureau (RB)'
  | 'Public Grievance Redressal Cell (PGRC)'
  | 'Approval Bureau (AB)'
  | 'Policy & Academic Planning Bureau (PAPB)';

export type KYCStatus = 'Not Started' | 'Pending' | 'Verified' | 'Failed';

export interface KYCRecord {
  status: KYCStatus;
  provider: 'DigiLocker Sandbox' | 'Gov Aadhaar e-KYC' | 'Institutional Verified' | 'Demonstration Mode';
  referenceId: string;
  verifiedAt?: string;
  complainantName?: string;
  contactMasked?: string;
  idType?: string;
  notes?: string;
}

export type EvidenceScreeningStatus = 
  | 'Not Screened'
  | 'Screening'
  | 'Screened — No AI Signal Detected'
  | 'Potential AI-Generated Content'
  | 'Screening Unavailable';

export interface HiveScreeningResult {
  status: EvidenceScreeningStatus;
  provider: 'Hive AI (api.thehive.ai)' | 'Hive AI Simulation Boundary';
  modelName: string; // e.g. 'hive-ai-generated-image-detection-v2'
  aiSignalPercentage: number; // 0 - 100
  confidenceScore: number;    // 0 - 100
  screenedAt: string;
  isFlaggedForHumanReview: boolean;
  explanation: string;
  modelVersion?: string;
  metadata?: Record<string, any>;
}

export type ReviewDecision = 
  | 'Accept for Further Review'
  | 'Request Additional Evidence'
  | 'Escalate for Investigation';

export interface OfficerEvidenceReview {
  reviewerId: string;
  reviewerName: string;
  bureau: Bureau;
  decision: ReviewDecision;
  reasoning: string;
  timestamp: string;
  actionTaken: string;
  internalConfidentialNote?: string;
}

export interface EvidenceItem {
  id: string;
  name: string;
  size: string;
  type: string; // 'image/jpeg' | 'image/png' | 'application/pdf' | etc.
  url?: string;
  uploadTimestamp: string;
  screening: HiveScreeningResult;
  review?: OfficerEvidenceReview;
}

export interface SupportingDocument {
  name: string;
  size: string;
  url?: string;
  type?: string;
  screeningStatus?: EvidenceScreeningStatus;
  aiScore?: number;
}

export interface TimelineEvent {
  date: string;
  officer: string;
  bureau: string;
  action: string;
  remarks: string;
}

export interface Complaint {
  caseId: string;
  aicteId: string;
  instName: string;
  category: string;
  title: string;
  description: string;
  complainantType: 'Faculty Member' | 'Student / Parent' | 'Whistleblower' | 'Anonymous';
  complainantName?: string;
  complainantEmail?: string;
  complainantPhone?: string;
  dateReceived: string;
  incidentDate?: string;
  incidentLocation?: string;
  assignedBureau: Bureau;
  assignedOfficer: string;
  priority: Priority;
  status: ComplaintStatus;
  lastAction: string;
  lastActionDate: string;
  nextAction: string;
  expectedDisposalDate: string;
  isOverdue: boolean;
  ageInDays: number;
  docs: SupportingDocument[];
  evidenceItems?: EvidenceItem[];
  kycRecord?: KYCRecord;
  linkedCaseIds: string[];
  timeline: TimelineEvent[];
  internalOfficerRemarks?: string;
  region?: string;
}

export interface Institution {
  id: string; // AICTE Permanent ID
  name: string;
  type: string;
  state: string;
  region: string;
  address: string;
  head: string;
  email: string;
  status: string;
  regulatoryActions: string[];
  linkedCases: string[];
  affiliatedUniversityId?: string;
}

export interface University {
  id: string;
  name: string;
  type: string; // 'State Technical University' | 'Central University' | 'Deemed University'
  state: string;
  region: string;
  registrar: string;
  email: string;
  phone: string;
  status: string;
  affiliatedInstitutionIds: string[];
}

export interface OverlapPair {
  caseA: Complaint;
  caseB: Complaint;
  score: number;
  reasons: string[];
  isLinked: boolean;
}

export interface NotificationItem {
  id: string;
  title: string;
  desc: string;
  time: string;
  type: 'OVERLAP' | 'OVERDUE' | 'ESCALATION' | 'STATUS_CHANGE' | 'EVIDENCE_REVIEW';
  targetCase?: string;
  read: boolean;
}

export interface AuditEvent {
  id: string;
  timestamp: string;
  actorId: string;
  actorName: string;
  actorRole: Role;
  action: string;
  targetType: 'COMPLAINT' | 'USER' | 'INSTITUTION' | 'EVIDENCE' | 'SYSTEM';
  targetId: string;
  details: string;
}

export interface User {
  id: string;
  name: string;
  email: string;
  role: Role;
  orgName?: string;
  aicteId?: string;
  phone?: string;
  status: 'active' | 'pending_approval' | 'suspended';
  passwordHash?: string;
  registeredAt: string;
  approvedBy?: string;
  approvedAt?: string;
}
