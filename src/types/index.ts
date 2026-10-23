export type Role = 'rb_officer' | 'pgrc_officer' | 'admin' | 'ro_officer' | 'senior_mgmt';

export type Priority = 'Urgent' | 'High' | 'Medium' | 'Low';

export type ComplaintStatus = 'Pending' | 'Under Process' | 'Disposed' | 'Transferred' | 'Escalated';

export type Bureau = 
  | 'Regulation Bureau (RB)'
  | 'Public Grievance Redressal Cell (PGRC)'
  | 'Approval Bureau (AB)'
  | 'Policy & Academic Planning Bureau (PAPB)';

export interface SupportingDocument {
  name: string;
  size: string;
  url?: string;
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
  dateReceived: string;
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
  linkedCaseIds: string[];
  timeline: TimelineEvent[];
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
  type: 'OVERLAP' | 'OVERDUE' | 'ESCALATION';
  targetCase?: string;
  read: boolean;
}
