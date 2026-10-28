import { Institution, Complaint, NotificationItem, User, University, AuditEvent } from '../types';

export const INITIAL_USERS: User[] = [
  {
    id: 'usr-1',
    name: 'Dr. Arvind Joshi',
    email: 'arvind.joshi@aicte-india.org',
    role: 'rb_officer',
    orgName: 'AICTE Headquarters (New Delhi)',
    aicteId: 'GOV-RB-01',
    phone: '+91 11 2958 1000',
    status: 'active',
    passwordHash: 'AICTE@RB2026',
    registeredAt: '2026-01-10'
  },
  {
    id: 'usr-2',
    name: 'Smt. Sunita Sharma',
    email: 'sunita.sharma@aicte-india.org',
    role: 'pgrc_officer',
    orgName: 'AICTE Headquarters (New Delhi)',
    aicteId: 'GOV-PGRC-02',
    phone: '+91 11 2958 1002',
    status: 'active',
    passwordHash: 'AICTE@PGRC2026',
    registeredAt: '2026-01-12'
  },
  {
    id: 'usr-3',
    name: 'Shri K. Ramanathan',
    email: 'admin@aicte-india.gov.in',
    role: 'admin',
    orgName: 'AICTE IT Enclave / NIC',
    aicteId: 'GOV-ADM-01',
    phone: '+91 11 2958 1010',
    status: 'active',
    passwordHash: 'AICTE@Admin2026',
    registeredAt: '2026-01-01'
  },
  {
    id: 'usr-4',
    name: 'Shri D. V. Kulkarni',
    email: 'wro.mumbai@aicte-india.org',
    role: 'ro_officer',
    orgName: 'Western Regional Office (Mumbai)',
    aicteId: 'GOV-WRO-01',
    phone: '+91 22 2285 5412',
    status: 'active',
    passwordHash: 'AICTE@WRO2026',
    registeredAt: '2026-01-15'
  },
  {
    id: 'usr-5',
    name: 'Prof. T. G. Sitharam',
    email: 'advisor.ms@aicte-india.org',
    role: 'senior_mgmt',
    orgName: 'AICTE Council Secretariat',
    aicteId: 'GOV-SEC-01',
    phone: '+91 11 2958 1001',
    status: 'active',
    passwordHash: 'AICTE@Gov2026',
    registeredAt: '2026-01-05'
  },
  {
    id: 'usr-6',
    name: 'Dr. S. K. Raman (Principal)',
    email: 'principal@apexinstitute.edu.in',
    role: 'college_inst',
    orgName: 'Apex Institute of Technology & Management',
    aicteId: '1-3324567891',
    phone: '+91 98230 45678',
    status: 'active',
    passwordHash: 'Apex@Inst2026',
    registeredAt: '2026-02-01'
  },
  {
    id: 'usr-7',
    name: 'Dr. R. C. Mathur (Registrar)',
    email: 'registrar@state-tech-univ.ac.in',
    role: 'university',
    orgName: 'State Technical University',
    aicteId: 'UNIV-MH-010',
    phone: '+91 94220 12345',
    status: 'active',
    passwordHash: 'Univ@Tech2026',
    registeredAt: '2026-02-10'
  }
];

export const INITIAL_UNIVERSITIES: University[] = [
  {
    id: "UNIV-MH-010",
    name: "State Technical University (Maharashtra)",
    type: "State Technical University",
    state: "Maharashtra",
    region: "Western Region (WRO)",
    registrar: "Dr. R. C. Mathur (Registrar)",
    email: "registrar@state-tech-univ.ac.in",
    phone: "+91 94220 12345",
    status: "Verified & Active",
    affiliatedInstitutionIds: ["1-3324567891"]
  },
  {
    id: "UNIV-UP-004",
    name: "Uttar Pradesh Technological University",
    type: "State Technical University",
    state: "Uttar Pradesh",
    region: "Northern Region (NRO)",
    registrar: "Prof. Vinay Pathak",
    email: "registrar@uptu-state.ac.in",
    phone: "+91 522 2772194",
    status: "Verified & Active",
    affiliatedInstitutionIds: ["1-4829103942"]
  },
  {
    id: "UNIV-KA-008",
    name: "Visvesvaraya Technological University",
    type: "State Technical University",
    state: "Karnataka",
    region: "South-Western Region (SWRO)",
    registrar: "Dr. B. E. Rangaswamy",
    email: "registrar@vtu.ac.in",
    phone: "+91 831 2498100",
    status: "Verified & Active",
    affiliatedInstitutionIds: ["1-5582910483"]
  }
];

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
    linkedCases: ["AICTE/RB/2026/0104", "AICTE/PGRC/2026/0218"],
    affiliatedUniversityId: "UNIV-MH-010"
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
    linkedCases: ["AICTE/RB/2026/0112", "AICTE/PGRC/2026/0225"],
    affiliatedUniversityId: "UNIV-UP-004"
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
    linkedCases: ["AICTE/PGRC/2026/0205"],
    affiliatedUniversityId: "UNIV-KA-008"
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
    complainantName: "Prof. Amit Verma",
    complainantEmail: "amit.verma.cse@gmail.com",
    complainantPhone: "+91 98230 99881",
    dateReceived: "2026-03-12",
    incidentDate: "2026-02-15",
    incidentLocation: "Campus Admin Block, Pune",
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
    region: "Western Region (WRO)",
    kycRecord: {
      status: "Verified",
      provider: "DigiLocker Sandbox",
      referenceId: "DL-KYC-2026-98124",
      verifiedAt: "2026-03-12 11:15 AM",
      complainantName: "Amit Verma",
      contactMasked: "+91 98230 XXXXX",
      idType: "Faculty ID & Aadhaar e-KYC",
      notes: "DigiLocker e-signature and institutional credential matched"
    },
    evidenceItems: [
      {
        id: "ev-104-1",
        name: "Salary_Slip_Discrepancy.pdf",
        size: "2.1 MB",
        type: "application/pdf",
        uploadTimestamp: "2026-03-12 11:18 AM",
        screening: {
          status: "Screening Unavailable",
          provider: "Hive AI (api.thehive.ai)",
          modelName: "hive-ai-generated-image-detection-v2",
          aiSignalPercentage: 0,
          confidenceScore: 0,
          screenedAt: "2026-03-12 11:19 AM",
          isFlaggedForHumanReview: false,
          explanation: "PDF document format. Hive image detection applies strictly to raster images (JPEG/PNG/WEBP). Document submitted for manual regulatory scrutiny."
        },
        review: {
          reviewerId: "usr-1",
          reviewerName: "Dr. Arvind Joshi",
          bureau: "Regulation Bureau (RB)",
          decision: "Accept for Further Review",
          reasoning: "Salary slip reflects Rs 32,500 vs 7th CPC mandated Rs 57,700 entry pay. Bank credit discrepancy corroborated.",
          timestamp: "2026-03-15 03:50 PM",
          actionTaken: "Issued notice to Registrar to submit Form 16 certified by CA."
        }
      },
      {
        id: "ev-104-2",
        name: "CS_Dept_Attendance_Photo.jpg",
        size: "1.4 MB",
        type: "image/jpeg",
        uploadTimestamp: "2026-03-12 11:20 AM",
        screening: {
          status: "Screened — No AI Signal Detected",
          provider: "Hive AI (api.thehive.ai)",
          modelName: "hive-ai-generated-image-detection-v2",
          aiSignalPercentage: 4,
          confidenceScore: 96,
          screenedAt: "2026-03-12 11:21 AM",
          isFlaggedForHumanReview: false,
          explanation: "Raster analysis indicates organic camera sensor characteristics, genuine EXIF metadata, and no synthesis artifacts. Probabilistic indicator only."
        },
        review: {
          reviewerId: "usr-1",
          reviewerName: "Dr. Arvind Joshi",
          bureau: "Regulation Bureau (RB)",
          decision: "Accept for Further Review",
          reasoning: "Noticeboard attendance register photograph shows 4 absent names marked with proxy ticks.",
          timestamp: "2026-03-15 03:52 PM",
          actionTaken: "Included in notice questionnaire."
        }
      }
    ],
    docs: [
      { name: "Salary_Slip_Discrepancy.pdf", size: "2.1 MB", type: "application/pdf", screeningStatus: "Screening Unavailable", aiScore: 0 },
      { name: "CS_Dept_Attendance_Photo.jpg", size: "1.4 MB", type: "image/jpeg", screeningStatus: "Screened — No AI Signal Detected", aiScore: 4 }
    ],
    linkedCaseIds: ["AICTE/PGRC/2026/0218"],
    timeline: [
      { date: "12 Mar 2026, 11:20 AM", officer: "Portal Intake Engine", bureau: "RB", action: "Complaint Lodged", remarks: "Petition received via National Grievance Portal after KYC clearance" },
      { date: "15 Mar 2026, 03:45 PM", officer: "Dr. Arvind Joshi", bureau: "RB", action: "Admitted & Assigned", remarks: "Prima facie evidence warrants verification under AICTE Regulations Clause 4.2" },
      { date: "10 Apr 2026, 02:00 PM", officer: "Dr. Arvind Joshi", bureau: "RB", action: "Show Cause Issued", remarks: "15 days granted to institution management for explanation" }
    ],
    internalOfficerRemarks: "High overlap with PGRC grievance AICTE/PGRC/2026/0218. Coordinated hearing proposed before Standing Hearing Committee."
  },
  {
    caseId: "AICTE/PGRC/2026/0218",
    aicteId: "1-3324567891",
    instName: "Apex Institute of Technology & Management",
    category: "Withholding of Original Certificates",
    title: "Faculty Grievance on 6 Months Unpaid Salaries and Original Degree Retention",
    description: "Grievance petition by 14 Assistant Professors stating the college has withheld original PhD/M.Tech degree certificates upon resignation and has not disbursed pending salary arrears for 6 months.",
    complainantType: "Faculty Member",
    complainantName: "Dr. Sneha Patil",
    complainantEmail: "sneha.patil.pune@gmail.com",
    complainantPhone: "+91 94220 55112",
    dateReceived: "2026-03-20",
    incidentDate: "2026-03-01",
    incidentLocation: "Administration Registrar Office, Pune",
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
    region: "Western Region (WRO)",
    kycRecord: {
      status: "Verified",
      provider: "DigiLocker Sandbox",
      referenceId: "DL-KYC-2026-88741",
      verifiedAt: "2026-03-20 09:50 AM",
      complainantName: "Dr. Sneha Patil",
      contactMasked: "+91 94220 XXXXX",
      idType: "Aadhaar e-KYC & Mobile OTP",
      notes: "DigiLocker document exchange verified authentic credentials"
    },
    evidenceItems: [
      {
        id: "ev-218-1",
        name: "Resignation_Receipt_Stamped.png",
        size: "940 KB",
        type: "image/png",
        uploadTimestamp: "2026-03-20 09:55 AM",
        screening: {
          status: "Screened — No AI Signal Detected",
          provider: "Hive AI (api.thehive.ai)",
          modelName: "hive-ai-generated-image-detection-v2",
          aiSignalPercentage: 3,
          confidenceScore: 97,
          screenedAt: "2026-03-20 09:56 AM",
          isFlaggedForHumanReview: false,
          explanation: "Clean document scan with authentic ink bleed and rubber stamp impression. Low AI synthetic probability."
        },
        review: {
          reviewerId: "usr-2",
          reviewerName: "Smt. Sunita Sharma",
          bureau: "Public Grievance Redressal Cell (PGRC)",
          decision: "Accept for Further Review",
          reasoning: "Acknowledgment receipt confirms submission of original degrees upon appointment in July 2022.",
          timestamp: "2026-03-24 04:20 PM",
          actionTaken: "Issued mandatory 7-day compliance directive to college Principal."
        }
      }
    ],
    docs: [
      { name: "Resignation_Receipt_Stamped.png", size: "940 KB", type: "image/png", screeningStatus: "Screened — No AI Signal Detected", aiScore: 3 }
    ],
    linkedCaseIds: ["AICTE/RB/2026/0104"],
    timeline: [
      { date: "20 Mar 2026, 10:00 AM", officer: "Intake Officer", bureau: "PGRC", action: "Grievance Registered", remarks: "Direct petition from faculty body" },
      { date: "24 Mar 2026, 04:15 PM", officer: "Smt. Sunita Sharma", bureau: "PGRC", action: "Ombudsman Notice", remarks: "Notice issued to return original certificates within 7 days" },
      { date: "14 Apr 2026, 11:30 AM", officer: "Smt. Sunita Sharma", bureau: "PGRC", action: "Hearing Scheduled", remarks: "Hearing conducted; Institute failed to produce return receipts" }
    ],
    internalOfficerRemarks: "AICTE Regulation prohibit retaining original certificates. Violation attracts punitive reduction of intake."
  },
  {
    caseId: "AICTE/RB/2026/0112",
    aicteId: "1-4829103942",
    instName: "National Polytechnic & Science Academy",
    category: "Unapproved Course Intake",
    title: "Unapproved Student Admissions Exceeding AICTE Approved Intake by 120 Seats",
    description: "Institute admitted 240 students in Diploma Mechanical & Electrical streams against approved intake of 120 seats, collecting capitation fees.",
    complainantType: "Whistleblower",
    complainantName: "Confidential Citizen Whistleblower",
    dateReceived: "2026-02-10",
    incidentDate: "2026-01-20",
    incidentLocation: "Ghaziabad, Uttar Pradesh",
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
    region: "Northern Region (NRO)",
    kycRecord: {
      status: "Verified",
      provider: "Gov Aadhaar e-KYC",
      referenceId: "GOV-AADH-2026-44321",
      verifiedAt: "2026-02-10 09:25 AM",
      complainantName: "Protected Whistleblower",
      contactMasked: "+91 99100 XXXXX",
      idType: "Aadhaar Virtual ID (VID)",
      notes: "Identity verified securely; identity masked under Whistleblower Protection Act."
    },
    evidenceItems: [
      {
        id: "ev-112-1",
        name: "Admission_List_Discrepancy.jpg",
        size: "3.5 MB",
        type: "image/jpeg",
        uploadTimestamp: "2026-02-10 09:28 AM",
        screening: {
          status: "Potential AI-Generated Content",
          provider: "Hive AI (api.thehive.ai)",
          modelName: "hive-ai-generated-image-detection-v2",
          aiSignalPercentage: 88,
          confidenceScore: 91,
          screenedAt: "2026-02-10 09:30 AM",
          isFlaggedForHumanReview: true,
          explanation: "High AI synthesis signal detected. Digital artifacts consistent with generative text replacement. Flagged for mandatory forensic inspection before taking punitive action."
        },
        review: {
          reviewerId: "usr-1",
          reviewerName: "Dr. Arvind Joshi",
          bureau: "Regulation Bureau (RB)",
          decision: "Escalate for Investigation",
          reasoning: "Hive AI flagged image as potential synthetic modification. Cross-checked with state technical board enrollment database; excess admissions confirmed independently of the flagged image.",
          timestamp: "2026-02-15 02:10 PM",
          actionTaken: "Ordered surprise physical inspection by Northern Regional Office to seize physical admission ledgers."
        }
      }
    ],
    docs: [
      { name: "Admission_List_Discrepancy.jpg", size: "3.5 MB", type: "image/jpeg", screeningStatus: "Potential AI-Generated Content", aiScore: 88 }
    ],
    linkedCaseIds: ["AICTE/PGRC/2026/0225"],
    timeline: [
      { date: "10 Feb 2026, 09:30 AM", officer: "Portal Intake", bureau: "RB", action: "Lodged", remarks: "Whistleblower petition verified" },
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
    complainantName: "Rohan Tripathi",
    complainantEmail: "rohan.tripathi2024@gmail.com",
    dateReceived: "2026-02-18",
    incidentDate: "2026-02-10",
    incidentLocation: "Accounts Office, Ghaziabad",
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
    region: "Northern Region (NRO)",
    kycRecord: {
      status: "Verified",
      provider: "DigiLocker Sandbox",
      referenceId: "DL-KYC-2026-55912",
      verifiedAt: "2026-02-18 01:45 PM",
      complainantName: "Rohan Tripathi",
      contactMasked: "+91 98390 XXXXX",
      idType: "Student ID Card & DigiLocker Aadhaar",
      notes: "Student enrollment verified"
    },
    evidenceItems: [
      {
        id: "ev-225-1",
        name: "Fee_Receipts_BuildingFund.jpg",
        size: "1.8 MB",
        type: "image/jpeg",
        uploadTimestamp: "2026-02-18 01:50 PM",
        screening: {
          status: "Screened — No AI Signal Detected",
          provider: "Hive AI (api.thehive.ai)",
          modelName: "hive-ai-generated-image-detection-v2",
          aiSignalPercentage: 6,
          confidenceScore: 94,
          screenedAt: "2026-02-18 01:52 PM",
          isFlaggedForHumanReview: false,
          explanation: "Receipt image shows genuine dot-matrix print characteristics and handwritten signature."
        },
        review: {
          reviewerId: "usr-2",
          reviewerName: "Smt. Sunita Sharma",
          bureau: "Public Grievance Redressal Cell (PGRC)",
          decision: "Accept for Further Review",
          reasoning: "Receipt explicitly titles Rs 50,000 as 'Unapproved Building Amenity Levy' in violation of Section 6 of AICTE Guidelines.",
          timestamp: "2026-02-22 10:15 AM",
          actionTaken: "Issued show cause to Finance Officer."
        }
      }
    ],
    docs: [
      { name: "Fee_Receipts_BuildingFund.jpg", size: "1.8 MB", type: "image/jpeg", screeningStatus: "Screened — No AI Signal Detected", aiScore: 6 }
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
    complainantName: "Vikas Reddy",
    complainantEmail: "vikas.reddy99@gmail.com",
    dateReceived: "2026-01-15",
    incidentDate: "2025-12-28",
    incidentLocation: "Bengaluru, Karnataka",
    assignedBureau: "Public Grievance Redressal Cell (PGRC)",
    assignedOfficer: "Smt. Sunita Sharma (Deputy Director, PGRC)",
    priority: "Medium",
    status: "Resolved",
    lastAction: "Case resolved & disposed: Full refund of Rs 1,44,000 credited to student account with Rs 1,000 processing fee deduction as per norms",
    lastActionDate: "2026-03-25",
    nextAction: "None (Closed)",
    expectedDisposalDate: "2026-03-30",
    isOverdue: false,
    ageInDays: 69,
    region: "South-Western Region (SWRO)",
    kycRecord: {
      status: "Verified",
      provider: "DigiLocker Sandbox",
      referenceId: "DL-KYC-2026-11234",
      verifiedAt: "2026-01-15 10:45 AM",
      complainantName: "Vikas Reddy",
      contactMasked: "+91 97410 XXXXX",
      idType: "Aadhaar e-KYC"
    },
    evidenceItems: [
      {
        id: "ev-205-1",
        name: "Bank_NEFT_RefundProof.pdf",
        size: "850 KB",
        type: "application/pdf",
        uploadTimestamp: "2026-03-25 04:00 PM",
        screening: {
          status: "Screening Unavailable",
          provider: "Hive AI (api.thehive.ai)",
          modelName: "hive-ai-generated-image-detection-v2",
          aiSignalPercentage: 0,
          confidenceScore: 0,
          screenedAt: "2026-03-25 04:05 PM",
          isFlaggedForHumanReview: false,
          explanation: "Bank statement PDF submitted by Institution verifying refund transaction UTR #7728190."
        },
        review: {
          reviewerId: "usr-2",
          reviewerName: "Smt. Sunita Sharma",
          bureau: "Public Grievance Redressal Cell (PGRC)",
          decision: "Accept for Further Review",
          reasoning: "Transaction verified with ICICI Bank clearing. Full restitution achieved.",
          timestamp: "2026-03-25 05:00 PM",
          actionTaken: "Grievance marked as Resolved and Closed."
        }
      }
    ],
    docs: [
      { name: "Bank_NEFT_RefundProof.pdf", size: "850 KB", type: "application/pdf", screeningStatus: "Screening Unavailable", aiScore: 0 }
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
    region: "North-West Region (NWRO)",
    kycRecord: {
      status: "Verified",
      provider: "Institutional Verified",
      referenceId: "INST-VERIF-2026-0091",
      verifiedAt: "2026-04-02 01:10 PM",
      complainantName: "Internal AICTE Inspectorate",
      idType: "Official EOA Scrutiny Report"
    },
    docs: [
      { name: "Inspection_Deficiency_Report.pdf", size: "3.4 MB", type: "application/pdf", screeningStatus: "Screening Unavailable", aiScore: 0 }
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
    complainantName: "Dr. K. Swaminathan",
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
    region: "Southern Region (SRO)",
    kycRecord: {
      status: "Verified",
      provider: "DigiLocker Sandbox",
      referenceId: "DL-KYC-2026-99231",
      verifiedAt: "2026-03-05 08:50 AM",
      complainantName: "Dr. K. Swaminathan",
      contactMasked: "+91 98400 XXXXX",
      idType: "Faculty Aadhaar e-KYC"
    },
    docs: [
      { name: "Lab_Photographs_EquipmentList.pdf", size: "5.1 MB", type: "application/pdf", screeningStatus: "Screening Unavailable", aiScore: 0 }
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
  },
  {
    id: "nt-4",
    title: "Hive AI Screening Flagged: AICTE/RB/2026/0112",
    desc: "Evidence Admission_List_Discrepancy.jpg flagged with 88% AI signal.",
    time: "2h ago",
    type: "EVIDENCE_REVIEW",
    targetCase: "AICTE/RB/2026/0112",
    read: false
  }
];

export const INITIAL_AUDIT_LOGS: AuditEvent[] = [
  {
    id: "aud-001",
    timestamp: "2026-04-18 15:00:22",
    actorId: "usr-1",
    actorName: "Dr. Arvind Joshi",
    actorRole: "rb_officer",
    action: "ESCALATE_CASE",
    targetType: "COMPLAINT",
    targetId: "AICTE/RB/2026/0112",
    details: "Case escalated to Member Secretary due to severe unapproved intake violations exceeding 120 seats."
  },
  {
    id: "aud-002",
    timestamp: "2026-04-14 11:32:10",
    actorId: "usr-2",
    actorName: "Smt. Sunita Sharma",
    actorRole: "pgrc_officer",
    action: "SCHEDULE_HEARING",
    targetType: "COMPLAINT",
    targetId: "AICTE/PGRC/2026/0218",
    details: "Ombudsman hearing scheduled for Apex Institute of Technology & Management on degree retention."
  },
  {
    id: "aud-003",
    timestamp: "2026-04-10 14:02:45",
    actorId: "usr-1",
    actorName: "Dr. Arvind Joshi",
    actorRole: "rb_officer",
    action: "ISSUE_SHOW_CAUSE",
    targetType: "COMPLAINT",
    targetId: "AICTE/RB/2026/0104",
    details: "Show cause notice served under AICTE Regulation 4.2 requiring audited salary disbursements."
  },
  {
    id: "aud-004",
    timestamp: "2026-04-01 09:15:00",
    actorId: "usr-3",
    actorName: "Shri K. Ramanathan",
    actorRole: "admin",
    action: "USER_APPROVAL",
    targetType: "USER",
    targetId: "usr-6",
    details: "Approved College/Institution access for Apex Institute of Technology & Management (1-3324567891)."
  },
  {
    id: "aud-005",
    timestamp: "2026-03-25 17:00:15",
    actorId: "usr-2",
    actorName: "Smt. Sunita Sharma",
    actorRole: "pgrc_officer",
    action: "DISPOSE_COMPLAINT",
    targetType: "COMPLAINT",
    targetId: "AICTE/PGRC/2026/0205",
    details: "Disposed complaint after verified refund credit of Rs 1,44,000 via UTR #7728190."
  }
];
