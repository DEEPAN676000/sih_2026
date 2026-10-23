import { Institution, Complaint, NotificationItem } from '../types';

export const INITIAL_INSTITUTIONS: Institution[] = [
  {
    id: "1-3324567891",
    name: "Apex Institute of Technology & Management",
    type: "Engineering & Technology",
    state: "Maharashtra",
    region: "Western Region (WRO)",
    address: "Sector 15, Knowledge Park, Pune, MH - 411057",
    head: "Dr. S. K. Raman (Principal)",
    email: "principal@apexinstitute.edu.in",
    status: "Approved (EOA 2025-26)",
    regulatoryActions: [
      "Show Cause Notice issued under RB Reg. 4.2 (Salary Deficiencies)",
      "Directive issued to constitute Internal Grievance Committee"
    ],
    linkedCases: ["AICTE/RB/2026/0104", "AICTE/PGRC/2026/0218"]
  },
  {
    id: "1-4829103942",
    name: "National Polytechnic & Science Academy",
    type: "Polytechnic / Diploma",
    state: "Uttar Pradesh",
    region: "Northern Region (NRO)",
    address: "NH-24 Bypass, Ghaziabad, UP - 201009",
    head: "Prof. Rajeshwar Verma",
    email: "director@nationalpoly.org.in",
    status: "Approved with Cautions",
    regulatoryActions: [
      "Physical Inspection conducted by Northern Regional Office",
      "Excess intake admission blocked for Academic Year 2026-27"
    ],
    linkedCases: ["AICTE/RB/2026/0112", "AICTE/PGRC/2026/0225"]
  },
  {
    id: "1-5582910483",
    name: "Imperial College of Engineering & Research",
    type: "Engineering & Technology",
    state: "Karnataka",
    region: "South-Western Region (SWRO)",
    address: "Electronic City Phase II, Bengaluru, KA - 560100",
    head: "Dr. Meenakshi Sundaram",
    email: "dean@imperialresearch.ac.in",
    status: "Approved (EOA 2025-26)",
    regulatoryActions: [
      "Compliance report verified on refund of security deposit"
    ],
    linkedCases: ["AICTE/PGRC/2026/0205"]
  },
  {
    id: "1-7729104851",
    name: "Vanguard School of Business & Management",
    type: "Management (PGDM)",
    state: "Delhi NCR",
    region: "North-West Region (NWRO)",
    address: "Institutional Area, Sector 62, Noida, NCR - 201301",
    head: "Dr. Alok Nath Chatterjee",
    email: "director@vanguardmba.edu",
    status: "Approved (EOA 2025-26)",
    regulatoryActions: [],
    linkedCases: ["AICTE/AB/2026/0091"]
  },
  {
    id: "1-9923847162",
    name: "Saraswati College of Pharmacy & Health",
    type: "Pharmacy",
    state: "Tamil Nadu",
    region: "Southern Region (SRO)",
    address: "Avinashi Road, Coimbatore, TN - 641014",
    head: "Dr. K. Swaminathan",
    email: "contact@saraswatipharmacy.edu",
    status: "Approved (EOA 2025-26)",
    regulatoryActions: [
      "Mandatory Laboratory upgrade notice issued"
    ],
    linkedCases: ["AICTE/RB/2026/0099"]
  }
];

export const INITIAL_COMPLAINTS: Complaint[] = [
  {
    caseId: "AICTE/RB/2026/0104",
    aicteId: "1-3324567891",
    instName: "Apex Institute of Technology & Management",
    category: "Faculty Qualifications & Pay Scale Violation",
    title: "7th Pay Commission Non-compliance & Ghost Faculty in Computer Science Dept",
    description: "Complaint filed alleging that faculty members are receiving salaries 40% below AICTE 7th CPC guidelines, and cash kickbacks are demanded back. Furthermore, 4 faculty members listed on the AICTE portal are ghost faculty not present on campus.",
    complainantType: "Faculty Member",
    dateReceived: "2026-03-12",
    assignedBureau: "Regulation Bureau (RB)",
    assignedOfficer: "Dr. Arvind Joshi (Director, RB)",
    priority: "Urgent",
    status: "Under Process",
    lastAction: "Notice issued to Chairman demanding audited Form 16 and bank credit statements",
    lastActionDate: "2026-04-10",
    nextAction: "Scrutiny of bank salary credit sheets by Standing Hearing Committee",
    expectedDisposalDate: "2026-05-15",
    isOverdue: false,
    ageInDays: 42,
    docs: [
      { name: "Salary_Slip_Discrepancy.pdf", size: "2.1 MB" },
      { name: "Affidavit_Faculty_Signatures.pdf", size: "1.4 MB" }
    ],
    linkedCaseIds: ["AICTE/PGRC/2026/0218"],
    timeline: [
      { date: "12 Mar 2026, 11:20 AM", officer: "Portal Intake Engine", bureau: "RB", action: "Complaint Lodged", remarks: "Petition received via National Grievance Portal" },
      { date: "15 Mar 2026, 03:45 PM", officer: "Dr. Arvind Joshi", bureau: "RB", action: "Admitted & Assigned", remarks: "Prima facie evidence warrants verification under AICTE Regulations Clause 4.2" },
      { date: "10 Apr 2026, 02:00 PM", officer: "Dr. Arvind Joshi", bureau: "RB", action: "Show Cause Issued", remarks: "15 days granted to institution management for explanation" }
    ]
  },
  {
    caseId: "AICTE/PGRC/2026/0218",
    aicteId: "1-3324567891",
    instName: "Apex Institute of Technology & Management",
    category: "Withholding of Original Certificates",
    title: "Faculty Grievance on 6 Months Unpaid Salaries and Original Degree Retention",
    description: "Grievance petition by 14 Assistant Professors stating the college has withheld original PhD/M.Tech degree certificates upon resignation and has not disbursed pending salary arrears for 6 months.",
    complainantType: "Faculty Member",
    dateReceived: "2026-03-20",
    assignedBureau: "Public Grievance Redressal Cell (PGRC)",
    assignedOfficer: "Smt. Sunita Sharma (Deputy Director, PGRC)",
    priority: "Urgent",
    status: "Under Process",
    lastAction: "Summoned Principal for hearing before Ombudsman",
    lastActionDate: "2026-04-14",
    nextAction: "Joint inspection with Regulation Bureau recommended",
    expectedDisposalDate: "2026-05-01",
    isOverdue: false,
    ageInDays: 34,
    docs: [
      { name: "Grievance_Petition_Signed.pdf", size: "3.2 MB" },
      { name: "Resignation_Letters_List.pdf", size: "940 KB" }
    ],
    linkedCaseIds: ["AICTE/RB/2026/0104"],
    timeline: [
      { date: "20 Mar 2026, 10:00 AM", officer: "Intake Officer", bureau: "PGRC", action: "Grievance Registered", remarks: "Direct petition from faculty body" },
      { date: "24 Mar 2026, 04:15 PM", officer: "Smt. Sunita Sharma", bureau: "PGRC", action: "Ombudsman Notice", remarks: "Notice issued to return original certificates within 7 days" },
      { date: "14 Apr 2026, 11:30 AM", officer: "Smt. Sunita Sharma", bureau: "PGRC", action: "Hearing Scheduled", remarks: "Hearing conducted; Institute failed to produce return receipts" }
    ]
  },
  {
    caseId: "AICTE/RB/2026/0112",
    aicteId: "1-4829103942",
    instName: "National Polytechnic & Science Academy",
    category: "Unapproved Course Intake",
    title: "Unapproved Student Admissions Exceeding AICTE Approved Intake by 120 Seats",
    description: "Institute admitted 240 students in Diploma Mechanical & Electrical streams against approved intake of 120 seats, collecting capitation fees.",
    complainantType: "Whistleblower",
    dateReceived: "2026-02-10",
    assignedBureau: "Regulation Bureau (RB)",
    assignedOfficer: "Dr. Arvind Joshi (Director, RB)",
    priority: "High",
    status: "Escalated",
    lastAction: "Matter escalated to Member Secretary for approval of intake reduction",
    lastActionDate: "2026-04-18",
    nextAction: "Formal council resolution for penalty imposition",
    expectedDisposalDate: "2026-04-15",
    isOverdue: true,
    ageInDays: 72,
    docs: [
      { name: "Admission_List_Discrepancy.pdf", size: "4.5 MB" }
    ],
    linkedCaseIds: ["AICTE/PGRC/2026/0225"],
    timeline: [
      { date: "10 Feb 2026, 09:30 AM", officer: "Portal Intake", bureau: "RB", action: "Lodged", remarks: "Whistleblower petition" },
      { date: "18 Apr 2026, 03:00 PM", officer: "Dr. Arvind Joshi", bureau: "RB", action: "Escalated", remarks: "Exceeded SLA; escalated due to severe regulatory breach" }
    ]
  },
  {
    caseId: "AICTE/PGRC/2026/0225",
    aicteId: "1-4829103942",
    instName: "National Polytechnic & Science Academy",
    category: "Capitation Fee & Excess Tuition Fee",
    title: "Capitation Fee Extortion of Rs 50,000 for Exam Admit Cards",
    description: "Students report institute withholding examination admit cards demanding Rs 50,000 additional building fund not listed in AICTE fee structure.",
    complainantType: "Student / Parent",
    dateReceived: "2026-02-18",
    assignedBureau: "Public Grievance Redressal Cell (PGRC)",
    assignedOfficer: "Smt. Sunita Sharma (Deputy Director, PGRC)",
    priority: "Urgent",
    status: "Under Process",
    lastAction: "Direct warning sent to Chief Proctor for immediate release of admit cards",
    lastActionDate: "2026-04-05",
    nextAction: "Verification of admit card issuance receipts",
    expectedDisposalDate: "2026-04-20",
    isOverdue: true,
    ageInDays: 64,
    docs: [
      { name: "Fee_Receipts_BuildingFund.pdf", size: "1.8 MB" }
    ],
    linkedCaseIds: ["AICTE/RB/2026/0112"],
    timeline: [
      { date: "18 Feb 2026, 02:00 PM", officer: "Intake Desk", bureau: "PGRC", action: "Registered", remarks: "Student union representation" }
    ]
  },
  {
    caseId: "AICTE/PGRC/2026/0205",
    aicteId: "1-5582910483",
    instName: "Imperial College of Engineering & Research",
    category: "Denial of Refund on Admission Cancellation",
    title: "Non-Refund of Rs 1,45,000 Caution Money after Seat Surrender within Deadline",
    description: "Student cancelled B.Tech admission before cutoff date. College refused to refund the seat fees citing internal trust guidelines in violation of AICTE Refund Policy.",
    complainantType: "Student / Parent",
    dateReceived: "2026-01-15",
    assignedBureau: "Public Grievance Redressal Cell (PGRC)",
    assignedOfficer: "Smt. Sunita Sharma (Deputy Director, PGRC)",
    priority: "Medium",
    status: "Disposed",
    lastAction: "Case disposed: Full refund of Rs 1,44,000 credited to student account with Rs 1,000 processing fee deduction as per norms",
    lastActionDate: "2026-03-25",
    nextAction: "None (Closed)",
    expectedDisposalDate: "2026-03-30",
    isOverdue: false,
    ageInDays: 69,
    docs: [
      { name: "Bank_NEFT_RefundProof.pdf", size: "850 KB" }
    ],
    linkedCaseIds: [],
    timeline: [
      { date: "15 Jan 2026, 11:00 AM", officer: "Intake", bureau: "PGRC", action: "Registered", remarks: "Student grievance" },
      { date: "25 Mar 2026, 05:00 PM", officer: "Smt. Sunita Sharma", bureau: "PGRC", action: "Disposed", remarks: "Refund verified by bank transaction UTR #7728190" }
    ]
  },
  {
    caseId: "AICTE/AB/2026/0091",
    aicteId: "1-7729104851",
    instName: "Vanguard School of Business & Management",
    category: "Lack of Mandatory Laboratory Infrastructure",
    title: "Deficiency in Computing Facilities & Bloomberg Terminal Lab",
    description: "Inspection committee noted that mandatory computer-to-student ratio of 1:2 not met; simulation lab software licenses expired.",
    complainantType: "Anonymous",
    dateReceived: "2026-04-02",
    assignedBureau: "Approval Bureau (AB)",
    assignedOfficer: "Shri R. K. Mittal (Advisor, AB)",
    priority: "Medium",
    status: "Pending",
    lastAction: "Letter of deficiency issued with 30 days compliance timeline",
    lastActionDate: "2026-04-08",
    nextAction: "Submission of proof of software purchase and invoice upload",
    expectedDisposalDate: "2026-05-20",
    isOverdue: false,
    ageInDays: 21,
    docs: [
      { name: "Inspection_Deficiency_Report.pdf", size: "3.4 MB" }
    ],
    linkedCaseIds: [],
    timeline: [
      { date: "02 Apr 2026, 01:15 PM", officer: "Intake", bureau: "AB", action: "Inspection Flagged", remarks: "Discrepancy logged by EOA scrutiny team" }
    ]
  },
  {
    caseId: "AICTE/RB/2026/0099",
    aicteId: "1-9923847162",
    instName: "Saraswati College of Pharmacy & Health",
    category: "Lack of Mandatory Laboratory Infrastructure",
    title: "Deficient Animal House and Pharmacology Machine Room Equipment",
    description: "Pharmacology division operates without CPCSEA-approved animal house and machine room lacks tablet punch machines.",
    complainantType: "Faculty Member",
    dateReceived: "2026-03-05",
    assignedBureau: "Regulation Bureau (RB)",
    assignedOfficer: "Dr. Arvind Joshi (Director, RB)",
    priority: "High",
    status: "Pending",
    lastAction: "Southern Regional Officer instructed to conduct surprise verification",
    lastActionDate: "2026-04-12",
    nextAction: "Surprise inspection report submission",
    expectedDisposalDate: "2026-04-10",
    isOverdue: true,
    ageInDays: 48,
    docs: [
      { name: "Lab_Photographs_EquipmentList.pdf", size: "5.1 MB" }
    ],
    linkedCaseIds: [],
    timeline: [
      { date: "05 Mar 2026, 09:00 AM", officer: "Intake", bureau: "RB", action: "Lodged", remarks: "Faculty petition" }
    ]
  }
];

export const INITIAL_NOTIFICATIONS: NotificationItem[] = [
  {
    id: "nt-1",
    title: "Potential Inter-Bureau Overlap Alert",
    desc: "Apex Institute (1-3324567891) has concurrent cases in RB and PGRC.",
    time: "10m ago",
    type: "OVERLAP",
    targetCase: "AICTE/RB/2026/0104",
    read: false
  },
  {
    id: "nt-2",
    title: "Disposal SLA Overdue: AICTE/RB/2026/0112",
    desc: "National Polytechnic admission case is overdue by 8 days.",
    time: "1h ago",
    type: "OVERDUE",
    targetCase: "AICTE/RB/2026/0112",
    read: false
  },
  {
    id: "nt-3",
    title: "Escalation Action Approved",
    desc: "Case AICTE/RB/2026/0112 referred to Member Secretary.",
    time: "4h ago",
    type: "ESCALATION",
    targetCase: "AICTE/RB/2026/0112",
    read: false
  }
];
