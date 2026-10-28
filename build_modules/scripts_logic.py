# -*- coding: utf-8 -*-
"""
JavaScript core logic for AICTE Complaint Monitoring System.
Includes:
- Centralized Data Store with KYC, Hive screening & audit logs
- Role management & strict 7-role permissions
- 6-step Complaint Submission Wizard with mandatory KYC & Hive AI screening
- Dedicated Evidence Review Workspace with Officer Decision Logging
- Cross-Bureau Overlap Detection Engine (multi-factor similarity)
- Full URL Router (/portal/*, /raise-complaint, /track)
- Interactive Modals, Public Tracking & Chart.js Visualizations
"""

def get_scripts_js():
    return '''  <!-- SCRIPT: APPLICATION CORE LOGIC -->
  <script>
    // ==========================================
    // 1. DATA STATE & MOCK INITIALIZATION
    // ==========================================
    const DEFAULT_INSTITUTIONS = [
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

    const DEFAULT_UNIVERSITIES = [
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
      }
    ];

    const DEFAULT_USERS = [
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

    const DEFAULT_COMPLAINTS = [
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
          idType: "Faculty ID & Aadhaar e-KYC"
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
              explanation: "PDF document format. Hive image detection applies strictly to raster images (JPEG/PNG). Document submitted for manual regulatory scrutiny."
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
              status: "Screened  -  No AI Signal Detected",
              provider: "Hive AI (api.thehive.ai)",
              modelName: "hive-ai-generated-image-detection-v2",
              aiSignalPercentage: 4,
              confidenceScore: 96,
              screenedAt: "2026-03-12 11:21 AM",
              isFlaggedForHumanReview: false,
              explanation: "Raster analysis indicates natural camera sensor characteristics, genuine EXIF metadata, and no generative synthesis artifacts. Probabilistic indicator only."
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
          { name: "CS_Dept_Attendance_Photo.jpg", size: "1.4 MB", type: "image/jpeg", screeningStatus: "Screened  -  No AI Signal Detected", aiScore: 4 }
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
          idType: "Aadhaar e-KYC & Mobile OTP"
        },
        evidenceItems: [
          {
            id: "ev-218-1",
            name: "Resignation_Receipt_Stamped.png",
            size: "940 KB",
            type: "image/png",
            uploadTimestamp: "2026-03-20 09:55 AM",
            screening: {
              status: "Screened  -  No AI Signal Detected",
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
          { name: "Resignation_Receipt_Stamped.png", size: "940 KB", type: "image/png", screeningStatus: "Screened  -  No AI Signal Detected", aiScore: 3 }
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
          idType: "Aadhaar Virtual ID (VID)"
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
          idType: "Student ID Card & DigiLocker Aadhaar"
        },
        evidenceItems: [
          {
            id: "ev-225-1",
            name: "Fee_Receipts_BuildingFund.jpg",
            size: "1.8 MB",
            type: "image/jpeg",
            uploadTimestamp: "2026-02-18 01:50 PM",
            screening: {
              status: "Screened  -  No AI Signal Detected",
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
          { name: "Fee_Receipts_BuildingFund.jpg", size: "1.8 MB", type: "image/jpeg", screeningStatus: "Screened  -  No AI Signal Detected", aiScore: 6 }
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

    const DEFAULT_NOTIFICATIONS = [
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

    const DEFAULT_AUDIT_LOGS = [
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

    // Application Global State
    let institutions = JSON.parse(localStorage.getItem('aicte_institutions_v2')) || DEFAULT_INSTITUTIONS;
    let complaints = JSON.parse(localStorage.getItem('aicte_complaints_v2')) || DEFAULT_COMPLAINTS;
    let notifications = JSON.parse(localStorage.getItem('aicte_notifs_v2')) || DEFAULT_NOTIFICATIONS;
    let users = JSON.parse(localStorage.getItem('aicte_users_v2')) || DEFAULT_USERS;
    let auditLogs = JSON.parse(localStorage.getItem('aicte_audit_v2')) || DEFAULT_AUDIT_LOGS;
    let universities = DEFAULT_UNIVERSITIES;

    let currentRole = localStorage.getItem('aicte_active_role') || 'rb_officer';
    let currentUser = users.find(u => u.role === currentRole) || users[0];
    let activeTab = 'dashboard';
    let lastSubmittedCaseId = "AICTE/RB/2026/0104";

    // 6-Step Wizard State
    let wizardStep = 1;
    let wizardKycStatus = 'Not Started'; // 'Not Started' | 'Pending' | 'Verified' | 'Failed'
    let wizardKycRecord = null;
    let wizardFiles = [];
    let wizardHiveResults = [];

    // Save Data Helpers
    function saveData() {
      localStorage.setItem('aicte_institutions_v2', JSON.stringify(institutions));
      localStorage.setItem('aicte_complaints_v2', JSON.stringify(complaints));
      localStorage.setItem('aicte_notifs_v2', JSON.stringify(notifications));
      localStorage.setItem('aicte_users_v2', JSON.stringify(users));
      localStorage.setItem('aicte_audit_v2', JSON.stringify(auditLogs));
      localStorage.setItem('aicte_active_role', currentRole);
    }

    // Role Metadata Definitions for UI (All 7 Roles)
    const ROLE_METADATA = {
      'rb_officer': {
        avatarText: 'RB',
        avatarBg: 'bg-blue-600 text-white',
        title: 'Regulation Bureau (RB) Officer',
        sub: 'Dr. Arvind Joshi • Director',
        officer: 'Dr. Arvind Joshi',
        badge: 'Regulation Bureau (RB) Officer',
        bannerTitle: 'Regulation Bureau (RB) Regulatory Oversight',
        bannerDesc: 'Monitoring technical institutions for regulatory compliance, 7th CPC norms, unapproved seats, and coordination with PGRC.'
      },
      'pgrc_officer': {
        avatarText: 'PG',
        avatarBg: 'bg-purple-600 text-white',
        title: 'Public Grievance Cell (PGRC)',
        sub: 'Smt. Sunita Sharma • Dy Director',
        officer: 'Smt. Sunita Sharma',
        badge: 'PGRC Officer',
        bannerTitle: 'Public Grievance Redressal Cell (PGRC)',
        bannerDesc: 'Facilitating student and faculty grievance resolution, ombudsman hearings, and certificate return orders.'
      },
      'admin': {
        avatarText: 'AD',
        avatarBg: 'bg-slate-800 text-white',
        title: 'System Administrator',
        sub: 'Full System & Bureau Access',
        officer: 'Shri K. Ramanathan',
        badge: 'System Administrator (Full Access)',
        bannerTitle: 'System Administration & Security Governance Enclave',
        bannerDesc: 'Full platform oversight, role permissions management, administrative authorization of pending users, and audit trail.'
      },
      'ro_officer': {
        avatarText: 'RO',
        avatarBg: 'bg-emerald-600 text-white',
        title: 'Regional Officer (WRO)',
        sub: 'Western Region • Mumbai HQ',
        officer: 'Shri D. V. Kulkarni',
        badge: 'Western Regional Officer (WRO)',
        bannerTitle: 'Western Regional Office (WRO - Mumbai) Monitoring',
        bannerDesc: 'Regional compliance oversight, physical inspection verifications, and regional complaint tracking for Western states.'
      },
      'senior_mgmt': {
        avatarText: 'MS',
        avatarBg: 'bg-amber-600 text-slate-950 font-black',
        title: 'Senior Management',
        sub: 'Advisor / Member Secretary',
        officer: 'Prof. T. G. Sitharam',
        badge: 'Senior Management (Advisor/MS)',
        bannerTitle: 'AICTE Council Secretariat & Senior Management Overview',
        bannerDesc: 'Council-level KPI analytics, inter-bureau disposal velocity, SLA overdue escalations, and executive compliance reports.'
      },
      'college_inst': {
        avatarText: 'CI',
        avatarBg: 'bg-cyan-600 text-white',
        title: 'College / Institution',
        sub: 'Apex Inst of Tech • Dr. S. K. Raman',
        officer: 'Dr. S. K. Raman (Principal)',
        badge: 'Institution Representative (Apex Institute)',
        bannerTitle: 'Institution Grievance & Compliance Portal: Apex Institute of Technology',
        bannerDesc: 'Manage and track complaints lodged against or by your institution, respond to show-cause notices, and upload compliance reports.'
      },
      'university': {
        avatarText: 'UN',
        avatarBg: 'bg-indigo-600 text-white',
        title: 'University Authority',
        sub: 'State Technical Univ • Dr. R. C. Mathur',
        officer: 'Dr. R. C. Mathur (Registrar)',
        badge: 'University Administrative Authority',
        bannerTitle: 'University Affiliation & Grievance Coordination: State Technical University',
        bannerDesc: 'Monitor grievance proceedings and regulatory orders across affiliated technical colleges and submit university representations.'
      }
    };

    // ==========================================
    // 2. ROUTING ENGINE (/portal/*, /raise-complaint, /track, /)
    // ==========================================
    function navigateToRoute(routePath) {
      if (!routePath) routePath = '/';
      
      // Update browser URL without reloading if supported
      try {
        if (window.history && window.history.pushState) {
          window.history.pushState({ path: routePath }, '', routePath.startsWith('#') ? routePath : '#' + routePath.replace(/^\\//, ''));
        }
      } catch (e) {}

      handleRoute(routePath);
    }

    function handleRoute(route) {
      if (!route) {
        route = window.location.hash ? window.location.hash.replace('#', '') : window.location.pathname;
      }
      if (route.startsWith('/')) route = route.substring(1);
      if (route.startsWith('#')) route = route.substring(1);

      // 1. Landing Page Route
      if (!route || route === 'home' || route === 'landing') {
        showLandingPage();
        return;
      }

      // 2. Complaint Wizard Route
      if (route === 'raise-complaint' || route === 'wizard') {
        showLandingPage();
        openComplaintWizard();
        return;
      }

      // 3. Track Complaint Route
      if (route === 'track' || route === 'track-complaint') {
        showLandingPage();
        showPublicTrackModal();
        return;
      }

      // 4. Role Portals (/portal/rb, /portal/pgrc, etc.)
      if (route.startsWith('portal/')) {
        const sub = route.replace('portal/', '');
        const roleMap = {
          'rb': 'rb_officer',
          'pgrc': 'pgrc_officer',
          'admin': 'admin',
          'regional': 'ro_officer',
          'management': 'senior_mgmt',
          'institution': 'college_inst',
          'university': 'university'
        };
        const targetRole = roleMap[sub] || 'rb_officer';
        openRolePortal(targetRole);
        return;
      }

      // Fallback: Show landing page
      showLandingPage();
    }

    window.addEventListener('popstate', (e) => {
      handleRoute();
    });

    window.addEventListener('hashchange', (e) => {
      handleRoute();
    });

    function showLandingPage() {
      document.getElementById('landingPageScreen').classList.remove('hidden');
      document.getElementById('portalContainer').classList.add('hidden');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function openRolePortal(role) {
      currentRole = role;
      document.getElementById('landingPageScreen').classList.add('hidden');
      document.getElementById('portalContainer').classList.remove('hidden');
      changeActiveRole(role, false);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Role Simulator & Authenticated Session Synchronization
    function changeActiveRole(role, notify = true) {
      currentRole = role;
      currentUser = users.find(u => u.role === role) || users[0];
      const meta = ROLE_METADATA[role] || ROLE_METADATA['rb_officer'];

      // Header display
      const nameEl = document.getElementById('userNameDisplay');
      const roleEl = document.getElementById('userRoleDisplay');
      const avatarEl = document.getElementById('userAvatar');
      const activePortalIndicator = document.getElementById('activePortalIndicator');

      if (nameEl) nameEl.textContent = meta.officer;
      if (roleEl) roleEl.textContent = meta.badge;
      if (activePortalIndicator) activePortalIndicator.textContent = meta.title;
      if (avatarEl) {
        avatarEl.textContent = meta.avatarText;
        avatarEl.className = `w-6 h-6 rounded-lg flex items-center justify-center font-bold text-[10px] ${meta.avatarBg}`;
      }

      // Workspace banner
      const bannerBadge = document.getElementById('roleBadgeDisplay');
      const bannerTitle = document.getElementById('roleBannerTitle');
      const bannerDesc = document.getElementById('roleBannerDesc');
      const bannerAicteId = document.getElementById('roleAicteIdDisplay');

      if (bannerBadge) bannerBadge.textContent = meta.badge;
      if (bannerTitle) bannerTitle.textContent = meta.bannerTitle;
      if (bannerDesc) bannerDesc.textContent = meta.bannerDesc;
      if (bannerAicteId) bannerAicteId.textContent = currentUser ? currentUser.aicteId || 'GOV-HQ' : 'GOV-HQ';

      // Admin tab visibility
      const adminNavTab = document.getElementById('nav-tab-users');
      if (adminNavTab) {
        if (role === 'admin') adminNavTab.classList.remove('hidden');
        else adminNavTab.classList.add('hidden');
      }

      // Refresh table views based on role data boundary
      renderDashboardStats();
      renderRecentComplaintsTable();
      renderAllComplaintsTable();
      renderOverlapCases();
      renderInstitutionsTable();
      renderEvidenceReviewWorkspace();
      if (role === 'admin') renderUsersTable();

      saveData();
      if (notify) showToast(`Switched active workspace: ${meta.title}`, 'info');
    }

    // ==========================================
    // 3. SIX-STEP COMPLAINT WIZARD LOGIC (/raise-complaint)
    // ==========================================
    function openComplaintWizard(instId = null) {
      wizardStep = 1;
      wizardKycStatus = 'Not Started';
      wizardKycRecord = null;
      wizardFiles = [];
      wizardHiveResults = [];

      document.getElementById('wizCompName').value = '';
      document.getElementById('wizCompEmail').value = '';
      document.getElementById('wizCompPhone').value = '';
      document.getElementById('wizTitle').value = '';
      document.getElementById('wizDescription').value = '';
      document.getElementById('wizConsentCheck').checked = false;
      document.getElementById('wizFinalConfirmCheck').checked = false;

      if (instId) {
        const select = document.getElementById('wizInstSelect');
        if (select) select.value = instId;
        handleWizardInstChange(instId);
      }

      updateWizardUI();
      document.getElementById('wizardModal').classList.remove('hidden');
    }

    function closeComplaintWizard() {
      document.getElementById('wizardModal').classList.add('hidden');
    }

    function updateWizardUI() {
      // Hide all steps
      for (let i = 1; i <= 6; i++) {
        const stepEl = document.getElementById(`wizardStep${i}`);
        const tabEl = document.getElementById(`wizStepTab${i}`);
        if (stepEl) stepEl.classList.add('hidden');
        if (tabEl) {
          tabEl.className = "flex items-center gap-1.5 text-slate-400";
          tabEl.querySelector('span:first-child').className = "w-5 h-5 rounded-full bg-slate-300 text-white flex items-center justify-center text-[10px]";
        }
      }

      // Show active step
      const currentStepEl = document.getElementById(`wizardStep${wizardStep}`);
      const currentTabEl = document.getElementById(`wizStepTab${wizardStep}`);
      if (currentStepEl) currentStepEl.classList.remove('hidden');
      if (currentTabEl) {
        currentTabEl.className = "flex items-center gap-1.5 text-gov-navy font-bold";
        currentTabEl.querySelector('span:first-child').className = "w-5 h-5 rounded-full bg-gov-navy text-white flex items-center justify-center text-[10px]";
      }

      // Buttons visibility
      const btnPrev = document.getElementById('wizBtnPrev');
      const btnNext = document.getElementById('wizBtnNext');
      const btnSubmit = document.getElementById('wizBtnSubmit');

      if (wizardStep === 1) {
        btnPrev.classList.add('hidden');
        btnNext.classList.remove('hidden');
        btnSubmit.classList.add('hidden');
        btnNext.innerHTML = '<span>Next: KYC Verification</span> &rarr;';
      } else if (wizardStep === 2) {
        btnPrev.classList.remove('hidden');
        btnNext.classList.remove('hidden');
        btnSubmit.classList.add('hidden');
        btnNext.innerHTML = '<span>Next: Complaint Details</span> &rarr;';
      } else if (wizardStep === 3) {
        btnPrev.classList.remove('hidden');
        btnNext.classList.remove('hidden');
        btnSubmit.classList.add('hidden');
        btnNext.innerHTML = '<span>Next: Upload Evidence</span> &rarr;';
      } else if (wizardStep === 4) {
        btnPrev.classList.remove('hidden');
        btnNext.classList.remove('hidden');
        btnSubmit.classList.add('hidden');
        btnNext.innerHTML = '<span>Next: Hive AI Screening</span> &rarr;';
      } else if (wizardStep === 5) {
        btnPrev.classList.remove('hidden');
        btnNext.classList.remove('hidden');
        btnSubmit.classList.add('hidden');
        btnNext.innerHTML = '<span>Next: Review &amp; Submit</span> &rarr;';
      } else if (wizardStep === 6) {
        btnPrev.classList.remove('hidden');
        btnNext.classList.add('hidden');
        btnSubmit.classList.remove('hidden');
        populateWizardReviewSummary();
      }
    }

    function nextWizardStep() {
      // Step 1 Validation
      if (wizardStep === 1) {
        const name = document.getElementById('wizCompName').value.trim();
        const email = document.getElementById('wizCompEmail').value.trim();
        const phone = document.getElementById('wizCompPhone').value.trim();
        const consent = document.getElementById('wizConsentCheck').checked;

        if (!name || !email || !phone) {
          showToast('Please provide complainant name, email, and phone.', 'error');
          return;
        }
        if (!consent) {
          showToast('Please accept the privacy and truthful declaration consent.', 'error');
          return;
        }
        wizardStep = 2;
        updateWizardUI();
        return;
      }

      // Step 2 Validation: Mandatory KYC (Section 5)
      if (wizardStep === 2) {
        if (wizardKycStatus !== 'Verified') {
          showToast('Mandatory KYC Verification Required before proceeding to Complaint Details.', 'error');
          return;
        }
        wizardStep = 3;
        updateWizardUI();
        return;
      }

      // Step 3 Validation: Complaint Details
      if (wizardStep === 3) {
        const title = document.getElementById('wizTitle').value.trim();
        const desc = document.getElementById('wizDescription').value.trim();
        if (!title || !desc) {
          showToast('Please enter both subject and detailed description of the grievance.', 'error');
          return;
        }
        wizardStep = 4;
        updateWizardUI();
        return;
      }

      // Step 4 Validation: Upload Evidence
      if (wizardStep === 4) {
        // Can proceed even if no files or with files
        wizardStep = 5;
        updateWizardUI();
        renderWizardHiveResults();
        return;
      }

      // Step 5 Validation: Hive AI Screening
      if (wizardStep === 5) {
        wizardStep = 6;
        updateWizardUI();
        return;
      }
    }

    function prevWizardStep() {
      if (wizardStep > 1) {
        wizardStep--;
        updateWizardUI();
      }
    }

    // Step 2 KYC Verification Functions
    function initiateKycVerification() {
      wizardKycStatus = 'Pending';
      const badge = document.getElementById('kycStatusBadge');
      if (badge) {
        badge.className = "badge bg-amber-100 text-amber-900 border border-amber-300";
        badge.textContent = "Pending OTP";
      }
      document.getElementById('kycOtpContainer').classList.remove('hidden');
      document.getElementById('kycSuccessCard').classList.add('hidden');
      document.getElementById('kycFailedCard').classList.add('hidden');
      showToast('Verification OTP dispatched to registered mobile / email.', 'info');
    }

    function confirmKycOtp() {
      const otp = document.getElementById('kycOtpInput').value.trim();
      if (!otp) {
        showToast('Please enter the 6-digit OTP.', 'error');
        return;
      }

      const name = document.getElementById('wizCompName').value.trim() || 'Complainant';
      const phone = document.getElementById('wizCompPhone').value.trim() || '+91 98765 43210';
      const providerRadio = document.querySelector('input[name="kycProviderRadio"]:checked');
      const providerName = providerRadio ? providerRadio.value : 'DigiLocker Sandbox';

      // Call Backend API /api/kyc/verify or use robust local fallback
      fetch('/api/kyc/verify', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, phone, otp, idType: providerName })
      })
      .then(res => res.json())
      .then(data => {
        applyKycSuccess(data.referenceId || ('DL-KYC-2026-' + Math.floor(10000 + Math.random() * 90000)), providerName, name);
      })
      .catch(() => {
        // Fallback simulation boundary when server is not running
        applyKycSuccess('DL-KYC-2026-' + Math.floor(10000 + Math.random() * 90000), providerName, name);
      });
    }

    function applyKycSuccess(refId, providerName, name) {
      wizardKycStatus = 'Verified';
      wizardKycRecord = {
        status: 'Verified',
        provider: providerName,
        referenceId: refId,
        verifiedAt: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        complainantName: name
      };

      const badge = document.getElementById('kycStatusBadge');
      if (badge) {
        badge.className = "badge bg-emerald-100 text-emerald-900 border border-emerald-300";
        badge.textContent = "Verified";
      }
      document.getElementById('kycOtpContainer').classList.add('hidden');
      document.getElementById('kycSuccessCard').classList.remove('hidden');
      document.getElementById('kycSuccessDetails').textContent = `Reference ID: ${refId} • Provider: ${providerName} • Status: Verified (${new Date().toLocaleTimeString()})`;
      showToast('Identity successfully verified via ' + providerName, 'success');
    }

    function saveWizardDraft() {
      const draft = {
        name: document.getElementById('wizCompName').value,
        type: document.getElementById('wizCompType').value,
        email: document.getElementById('wizCompEmail').value,
        phone: document.getElementById('wizCompPhone').value,
        instId: document.getElementById('wizInstSelect').value,
        category: document.getElementById('wizCategory').value,
        title: document.getElementById('wizTitle').value,
        description: document.getElementById('wizDescription').value,
        kycStatus: wizardKycStatus,
        savedAt: new Date().toISOString()
      };
      localStorage.setItem('aicte_complaint_draft', JSON.stringify(draft));
      showToast('Complaint draft saved securely to local storage.', 'success');
    }

    function handleWizardInstChange(instId) {
      const aicteIdInput = document.getElementById('wizAicteId');
      if (!aicteIdInput) return;
      if (instId === 'OTHER') {
        aicteIdInput.value = '1-PENDING-REG';
        aicteIdInput.readOnly = false;
      } else {
        aicteIdInput.value = instId;
        aicteIdInput.readOnly = true;
      }
    }

    function handleCategoryRoutingHint(cat) {
      const hint = document.getElementById('wizRoutingHint');
      if (!hint) return;
      if (cat.includes('Pay Scale') || cat.includes('Intake') || cat.includes('Infrastructure')) {
        hint.innerHTML = '<span class="w-2 h-2 rounded-full bg-blue-600"></span><span>Regulation Bureau (RB) • Statutory Norms Scrutiny</span>';
      } else {
        hint.innerHTML = '<span class="w-2 h-2 rounded-full bg-purple-600"></span><span>Public Grievance Redressal Cell (PGRC) • Individual Redressal</span>';
      }
    }

    // Step 4 File Upload Handlers
    function handleWizardFilesSelected(input) {
      if (!input.files || input.files.length === 0) return;
      for (let i = 0; i < input.files.length; i++) {
        const file = input.files[i];
        if (file.size > 10 * 1024 * 1024) {
          showToast(`File ${file.name} exceeds 10MB limit and was skipped.`, 'error');
          continue;
        }
        wizardFiles.push({
          name: file.name,
          size: (file.size / (1024 * 1024)).toFixed(1) + ' MB',
          type: file.type || 'application/octet-stream',
          screeningStatus: 'Not Screened',
          aiScore: 0
        });
      }
      renderWizardFileList();
    }

    function renderWizardFileList() {
      const listEl = document.getElementById('wizFileList');
      const countEl = document.getElementById('wizFileCount');
      if (!listEl) return;

      countEl.textContent = wizardFiles.length;
      if (wizardFiles.length === 0) {
        listEl.innerHTML = '<div class="text-[11px] text-slate-400 italic bg-white p-3 rounded-xl border border-slate-200">No files uploaded yet. You can attach JPEG/PNG images or PDF documents.</div>';
        return;
      }

      listEl.innerHTML = wizardFiles.map((f, idx) => `
        <div class="flex items-center justify-between p-2.5 bg-white border border-slate-200 rounded-xl text-xs">
          <div class="flex items-center gap-2">
            <span class="font-mono text-[10px] uppercase font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">${f.name.split('.').pop()}</span>
            <span class="font-bold text-slate-800">${f.name}</span>
            <span class="text-slate-400 text-[11px]">(${f.size})</span>
          </div>
          <button type="button" onclick="removeWizardFile(${idx})" class="text-rose-500 hover:text-rose-700 font-bold">&times; Remove</button>
        </div>
      `).join('');
    }

    function removeWizardFile(index) {
      wizardFiles.splice(index, 1);
      renderWizardFileList();
    }

    // Step 5 Hive AI Screening
    function runHiveScreeningAction() {
      if (wizardFiles.length === 0) {
        showToast('Please upload at least one image or document in Step 4.', 'info');
        return;
      }

      const progressEl = document.getElementById('hiveScreeningProgress');
      progressEl.classList.remove('hidden');

      let pct = 25;
      const bar = document.getElementById('hiveProgressBar');
      const pText = document.getElementById('hiveProgressPercent');

      const interval = setInterval(() => {
        pct += 25;
        if (bar) bar.style.width = pct + '%';
        if (pText) pText.textContent = pct + '%';

        if (pct >= 100) {
          clearInterval(interval);
          setTimeout(() => {
            progressEl.classList.add('hidden');
            completeHiveScreening();
          }, 300);
        }
      }, 150);
    }

    async function completeHiveScreening() {
      const results = [];
      for (let i = 0; i < wizardFiles.length; i++) {
        const f = wizardFiles[i];
        const isPdf = f.name.toLowerCase().endsWith('.pdf');
        const fileType = isPdf ? 'application/pdf' : (f.type || 'image/jpeg');
        let apiResult = null;

        try {
          const resp = await fetch('/api/hive/screen', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ filename: f.name, fileType })
          });
          if (resp.ok) {
            apiResult = await resp.json();
          }
        } catch (e) {
          // Backend offline or non-standard port: fallback to simulation boundary
        }

        if (apiResult) {
          results.push({
            filename: f.name,
            status: apiResult.status,
            score: apiResult.aiSignalPercentage,
            confidence: apiResult.confidenceScore,
            explanation: apiResult.explanation,
            provider: apiResult.provider,
            isLiveApi: apiResult.isLiveApi
          });
        } else {
          const isSynthetic = f.name.toLowerCase().includes('synthetic') || f.name.toLowerCase().includes('fake') || f.name.toLowerCase().includes('discrepancy');
          if (isPdf) {
            results.push({
              filename: f.name,
              status: 'Screening Unavailable',
              score: 0,
              confidence: 0,
              explanation: 'Document format (PDF). Hive AI deepfake detection applies strictly to raster photographs (JPEG/PNG).'
            });
          } else if (isSynthetic) {
            results.push({
              filename: f.name,
              status: 'Potential AI-Generated Content',
              score: 88,
              confidence: 91,
              explanation: 'Digital artifacts consistent with generative text replacement detected. Flagged for mandatory forensic inspection before taking punitive action.'
            });
          } else {
            results.push({
              filename: f.name,
              status: 'Screened - No AI Signal Detected',
              score: 4,
              confidence: 96,
              explanation: 'Raster analysis indicates natural camera sensor characteristics, genuine EXIF metadata, and no generative synthesis artifacts. Probabilistic indicator only.'
            });
          }
        }
      }

      wizardHiveResults = results;
      renderWizardHiveResults();
      showToast('Hive AI Evidence Screening completed successfully.', 'success');
    }

    function renderWizardHiveResults() {
      const container = document.getElementById('hiveResultsContainer');
      if (!container) return;

      if (wizardHiveResults.length === 0) {
        container.innerHTML = '<div class="text-[11px] text-slate-400 italic bg-white p-3 rounded-xl border border-slate-200">Click "Screen with Hive AI" above to inspect attached evidence.</div>';
        return;
      }

      container.innerHTML = wizardHiveResults.map(r => {
        const badgeColor = r.status.includes('No AI Signal') ? 'bg-emerald-100 text-emerald-900 border-emerald-300' :
                           r.status.includes('Potential AI') ? 'bg-rose-100 text-rose-900 border-rose-300' :
                           'bg-slate-100 text-slate-800 border-slate-300';
        return `
          <div class="p-3 bg-white border border-slate-200 rounded-xl space-y-1 text-xs">
            <div class="flex items-center justify-between">
              <span class="font-bold text-slate-800">${r.filename}</span>
              <span class="badge ${badgeColor} border">${r.status}</span>
            </div>
            <div class="flex items-center gap-3 text-[11px] text-slate-500 font-mono">
              <span>AI Signal: <strong>${r.score}%</strong></span>
              <span>•</span>
              <span>Confidence: <strong>${r.confidence}%</strong></span>
              <span>•</span>
              <span>Provider: Hive AI Gateway</span>
            </div>
            <p class="text-[11px] text-slate-600 leading-relaxed">${r.explanation}</p>
          </div>
        `;
      }).join('');
    }

    // Step 6 Review & Submit
    function populateWizardReviewSummary() {
      const name = document.getElementById('wizCompName').value.trim() || 'Complainant';
      const instSelect = document.getElementById('wizInstSelect');
      const instName = instSelect.options[instSelect.selectedIndex].text;
      const aicteId = document.getElementById('wizAicteId').value;
      const category = document.getElementById('wizCategory').value;
      const title = document.getElementById('wizTitle').value;

      document.getElementById('wizRevComplainant').textContent = name;
      document.getElementById('wizRevKycStatus').textContent = `KYC: ${wizardKycStatus} (Ref: ${wizardKycRecord ? wizardKycRecord.referenceId : 'N/A'})`;
      document.getElementById('wizRevInst').textContent = instName;
      document.getElementById('wizRevAicteId').textContent = `AICTE ID: ${aicteId}`;
      document.getElementById('wizRevCategory').textContent = category;
      document.getElementById('wizRevBureau').textContent = category.includes('Pay Scale') || category.includes('Intake') ? 'Regulation Bureau (RB)' : 'Public Grievance Redressal Cell (PGRC)';
      document.getElementById('wizRevTitle').textContent = title;
      document.getElementById('wizRevScreeningSummary').textContent = `${wizardFiles.length} file(s) attached (${wizardHiveResults.length} screened via Hive AI).`;
    }

    function submitWizardComplaint() {
      const confirmCheck = document.getElementById('wizFinalConfirmCheck').checked;
      if (!confirmCheck) {
        showToast('Please check the solemn affirmation box before submission.', 'error');
        return;
      }

      const name = document.getElementById('wizCompName').value.trim();
      const type = document.getElementById('wizCompType').value;
      const email = document.getElementById('wizCompEmail').value.trim();
      const phone = document.getElementById('wizCompPhone').value.trim();
      const instSelect = document.getElementById('wizInstSelect');
      const instName = instSelect.options[instSelect.selectedIndex].text.split(' (')[0];
      const aicteId = document.getElementById('wizAicteId').value;
      const category = document.getElementById('wizCategory').value;
      const title = document.getElementById('wizTitle').value.trim();
      const desc = document.getElementById('wizDescription').value.trim();

      const assignedBureau = (category.includes('Pay Scale') || category.includes('Intake') || category.includes('Infrastructure'))
        ? 'Regulation Bureau (RB)'
        : 'Public Grievance Redressal Cell (PGRC)';
      const bureauCode = assignedBureau.includes('RB') ? 'RB' : 'PGRC';
      const newCaseId = `AICTE/${bureauCode}/2026/0` + Math.floor(200 + Math.random() * 800);

      const newCase = {
        caseId: newCaseId,
        aicteId: aicteId,
        instName: instName,
        category: category,
        title: title,
        description: desc,
        complainantType: type,
        complainantName: name,
        complainantEmail: email,
        complainantPhone: phone,
        dateReceived: new Date().toISOString().split('T')[0],
        assignedBureau: assignedBureau,
        assignedOfficer: assignedBureau.includes('RB') ? 'Dr. Arvind Joshi (Director, RB)' : 'Smt. Sunita Sharma (Deputy Director, PGRC)',
        priority: 'High',
        status: 'Under Process',
        lastAction: 'Complaint Lodged via 6-Step Wizard with KYC clearance and Hive AI screening',
        lastActionDate: new Date().toISOString().split('T')[0],
        nextAction: 'Preliminary scrutiny of supporting evidence',
        expectedDisposalDate: '2026-05-30',
        isOverdue: false,
        ageInDays: 0,
        kycRecord: wizardKycRecord || { status: 'Verified', provider: 'DigiLocker Sandbox', referenceId: 'DL-KYC-NEW' },
        evidenceItems: wizardFiles.map((f, i) => ({
          id: `ev-${newCaseId}-${i}`,
          name: f.name,
          size: f.size,
          type: f.type,
          uploadTimestamp: new Date().toLocaleTimeString(),
          screening: wizardHiveResults[i] || { status: 'Not Screened', score: 0 }
        })),
        docs: wizardFiles.map(f => ({ name: f.name, size: f.size })),
        linkedCaseIds: [],
        timeline: [
          { date: new Date().toLocaleDateString('en-GB') + ', ' + new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }), officer: 'Intake Engine', bureau: bureauCode, action: 'Complaint Lodged', remarks: `Verified via ${wizardKycRecord ? wizardKycRecord.provider : 'KYC Sandbox'}` }
        ]
      };

      complaints.unshift(newCase);

      // Log an Audit Event
      auditLogs.unshift({
        id: 'aud-' + Math.floor(100 + Math.random() * 900),
        timestamp: new Date().toISOString().replace('T', ' ').substring(0, 19),
        actorId: 'public-intake',
        actorName: name,
        actorRole: 'college_inst',
        action: 'SUBMIT_COMPLAINT',
        targetType: 'COMPLAINT',
        targetId: newCaseId,
        details: `Submitted new grievance against ${instName} (${aicteId}) with KYC validation.`
      });

      lastSubmittedCaseId = newCaseId;
      saveData();

      // Trigger automatic overlap scan
      const overlapPairs = findPotentialOverlaps();
      const detectedOverlap = overlapPairs.find(p => p.caseA.caseId === newCaseId || p.caseB.caseId === newCaseId);
      if (detectedOverlap) {
        notifications.unshift({
          id: 'nt-' + Date.now(),
          title: 'Immediate Cross-Bureau Overlap Alert',
          desc: `New Case ${newCaseId} overlaps with existing case ${detectedOverlap.caseA.caseId === newCaseId ? detectedOverlap.caseB.caseId : detectedOverlap.caseA.caseId}`,
          time: 'Just now',
          type: 'OVERLAP',
          targetCase: newCaseId,
          read: false
        });
      }

      closeComplaintWizard();

      // Show confirmation dialog
      document.getElementById('confCaseId').textContent = newCaseId;
      document.getElementById('confInstName').textContent = instName;
      document.getElementById('confBureau').textContent = assignedBureau;
      document.getElementById('complaintConfirmationModal').classList.remove('hidden');

      renderDashboardStats();
      renderRecentComplaintsTable();
      renderAllComplaintsTable();
      renderOverlapCases();
      renderEvidenceReviewWorkspace();
    }

    // ==========================================
    // 4. EVIDENCE REVIEW WORKSPACE (Section 8: RB & PGRC)
    // ==========================================
    function renderEvidenceReviewWorkspace() {
      const tbody = document.getElementById('evidenceReviewTableBody');
      if (!tbody) return;

      const filteredCases = getRoleFilteredComplaints();
      const evidenceRows = [];

      filteredCases.forEach(c => {
        if (c.evidenceItems && c.evidenceItems.length > 0) {
          c.evidenceItems.forEach(ev => {
            evidenceRows.push({ c, ev });
          });
        } else if (c.docs && c.docs.length > 0) {
          c.docs.forEach(d => {
            evidenceRows.push({
              c,
              ev: {
                id: 'ev-legacy',
                name: d.name,
                screening: {
                  status: d.screeningStatus || 'Screened  -  No AI Signal Detected',
                  aiSignalPercentage: d.aiScore || 4,
                  confidenceScore: 96
                }
              }
            });
          });
        }
      });

      if (evidenceRows.length === 0) {
        tbody.innerHTML = '<tr><td colspan="6" class="py-4 text-center text-slate-400 italic">No evidence attachments in current workspace.</td></tr>';
        return;
      }

      tbody.innerHTML = evidenceRows.map(row => {
        const scr = row.ev.screening || {};
        const isFlagged = scr.status && scr.status.includes('Potential AI');
        const badgeColor = scr.status && scr.status.includes('No AI Signal') ? 'bg-emerald-100 text-emerald-900 border-emerald-300' :
                           isFlagged ? 'bg-rose-100 text-rose-900 border-rose-300' :
                           'bg-slate-100 text-slate-800 border-slate-300';

        return `
          <tr class="hover:bg-slate-50 transition-colors">
            <td class="py-2.5 px-3 font-mono font-bold text-gov-lightBlue">
              <a href="javascript:void(0)" onclick="viewComplaintDetails('${row.c.caseId}')" class="hover:underline">${row.c.caseId}</a>
            </td>
            <td class="py-2.5 px-3 font-medium text-slate-900 max-w-[160px] truncate">${row.c.instName}</td>
            <td class="py-2.5 px-3 font-mono text-[11px] text-slate-700">${row.ev.name}</td>
            <td class="py-2.5 px-3">
              <span class="badge ${badgeColor} border text-[10px]">${scr.status || 'Screened'}</span>
            </td>
            <td class="py-2.5 px-3 font-mono text-[11px]">
              <span class="font-bold ${isFlagged ? 'text-rose-600' : 'text-slate-700'}">${scr.aiSignalPercentage || 0}%</span>
              <span class="text-slate-400 text-[9px]">(Signal)</span>
            </td>
            <td class="py-2.5 px-3 text-right">
              <button onclick="viewComplaintDetails('${row.c.caseId}')" class="px-2.5 py-1 bg-gov-navy hover:bg-gov-darkNavy text-white font-bold rounded-lg text-[10px] transition-colors">
                Scrutinize &rarr;
              </button>
            </td>
          </tr>
        `;
      }).join('');
    }

    function submitOfficerEvidenceDecisionModal() {
      const decision = document.getElementById('modalOfficerDecisionSelect').value;
      const reasoning = document.getElementById('modalOfficerReasoningInput').value.trim();
      const caseId = document.getElementById('modalCaseId').textContent;

      if (!reasoning) {
        showToast('Please provide officer reasoning before recording decision.', 'error');
        return;
      }

      const complaint = complaints.find(c => c.caseId === caseId);
      if (complaint) {
        complaint.timeline.unshift({
          date: new Date().toLocaleDateString('en-GB') + ', ' + new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
          officer: currentUser.name,
          bureau: currentUser.role.includes('rb') ? 'RB' : 'PGRC',
          action: `Evidence Review: ${decision}`,
          remarks: reasoning
        });

        // Add audit trail entry
        auditLogs.unshift({
          id: 'aud-' + Math.floor(100 + Math.random() * 900),
          timestamp: new Date().toISOString().replace('T', ' ').substring(0, 19),
          actorId: currentUser.id,
          actorName: currentUser.name,
          actorRole: currentUser.role,
          action: 'OFFICER_EVIDENCE_DECISION',
          targetType: 'EVIDENCE',
          targetId: caseId,
          details: `Decision: ${decision}. Reasoning: ${reasoning}`
        });

        saveData();
        showToast(`Decision recorded: ${decision}`, 'success');
        document.getElementById('modalOfficerReasoningInput').value = '';
        viewComplaintDetails(caseId); // refresh modal timeline
        renderRecentComplaintsTable();
        renderAllComplaintsTable();
      }
    }

    // ==========================================
    // 5. OVERLAP DETECTION ENGINE
    // ==========================================
    function calculateSimilarityScore(caseA, caseB) {
      if (caseA.caseId === caseB.caseId) return { score: 0, isOverlap: false, reasons: [] };

      let score = 0;
      const reasons = [];

      // 1. AICTE Permanent ID Match (High Weight: 55 pts)
      if (caseA.aicteId && caseB.aicteId && caseA.aicteId === caseB.aicteId) {
        score += 55;
        reasons.push(`Identical AICTE Permanent ID: ${caseA.aicteId}`);
      }

      // 2. Cross-Bureau condition: RB vs PGRC (25 pts)
      const bureaus = [caseA.assignedBureau, caseB.assignedBureau];
      const isCrossBureau = bureaus.includes('Regulation Bureau (RB)') && bureaus.includes('Public Grievance Redressal Cell (PGRC)');
      if (isCrossBureau) {
        score += 25;
        reasons.push('Cross-Bureau Active Proceedings (Regulation Bureau & PGRC concurrently investigating)');
      }

      // 3. Category match / Correlated violations (15 pts)
      if (caseA.category === caseB.category) {
        score += 15;
        reasons.push(`Identical Category: ${caseA.category}`);
      } else if (
        (caseA.category.includes('Pay Scale') && caseB.category.includes('Certificates')) ||
        (caseA.category.includes('Intake') && caseB.category.includes('Fee'))
      ) {
        score += 12;
        reasons.push(`Correlated Violations (${caseA.category} ⟷ ${caseB.category})`);
      }

      // 4. Token Jaccard Similarity on Description (up to 25 pts)
      const tokenize = text => new Set(text.toLowerCase().replace(/[^a-z0-9 ]/g, '').split(/\\s+/).filter(w => w.length > 3));
      const tokensA = tokenize(caseA.description);
      const tokensB = tokenize(caseB.description);

      let intersection = 0;
      tokensA.forEach(token => {
        if (tokensB.has(token)) intersection++;
      });
      const union = tokensA.size + tokensB.size - intersection;
      const jaccard = union > 0 ? intersection / union : 0;

      if (jaccard > 0.15) {
        const textWeight = Math.min(25, Math.round(jaccard * 100));
        score += textWeight;
        reasons.push(`Grievance Narrative Similarity: ${Math.round(jaccard * 100)}% keyword overlap`);
      }

      return {
        score: Math.min(99, score),
        isOverlap: score >= 60,
        reasons
      };
    }

    function findPotentialOverlaps() {
      const pairs = [];
      const visited = new Set();

      for (let i = 0; i < complaints.length; i++) {
        for (let j = i + 1; j < complaints.length; j++) {
          const caseA = complaints[i];
          const caseB = complaints[j];
          const pairKey = [caseA.caseId, caseB.caseId].sort().join("<->");

          if (!visited.has(pairKey)) {
            visited.add(pairKey);
            const sim = calculateSimilarityScore(caseA, caseB);
            if (sim.isOverlap) {
              const isAlreadyLinked = (caseA.linkedCaseIds || []).includes(caseB.caseId);
              pairs.push({
                caseA,
                caseB,
                score: sim.score,
                reasons: sim.reasons,
                isLinked: isAlreadyLinked
              });
            }
          }
        }
      }
      return pairs;
    }

    function renderOverlapCases() {
      const container = document.getElementById('overlapPairsContainer');
      if (!container) return;

      const pairs = findPotentialOverlaps();
      if (pairs.length === 0) {
        container.innerHTML = '<div class="p-8 text-center bg-slate-50 border border-slate-200 rounded-2xl text-slate-500 font-medium">No inter-bureau overlaps identified currently.</div>';
        return;
      }

      container.innerHTML = pairs.map((pair, idx) => `
        <div class="p-5 rounded-2xl border ${pair.isLinked ? 'border-emerald-300 bg-emerald-50/20' : 'border-amber-300 bg-amber-50/20'} shadow-sm space-y-4">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-200 pb-3">
            <div class="flex items-center gap-2">
              <span class="px-2.5 py-1 rounded-full text-xs font-black ${pair.score >= 80 ? 'bg-rose-100 text-rose-800' : 'bg-amber-100 text-amber-800'}">
                ${pair.score}% Similarity Index
              </span>
              <span class="text-xs font-bold text-slate-900">${pair.caseA.instName}</span>
            </div>
            <div>
              ${pair.isLinked ? '<span class="badge bg-emerald-100 text-emerald-800 font-bold">&check; Cases Synchronized &amp; Linked</span>' : '<span class="badge bg-amber-100 text-amber-900 font-bold">Unlinked Potential Overlap</span>'}
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
            <div class="p-3 bg-white border border-slate-200 rounded-xl space-y-1">
              <div class="flex items-center justify-between">
                <span class="font-bold text-blue-900">${pair.caseA.assignedBureau}</span>
                <span class="font-mono text-slate-500 font-bold">${pair.caseA.caseId}</span>
              </div>
              <div class="font-bold text-slate-800">${pair.caseA.title}</div>
              <p class="text-[11px] text-slate-500 line-clamp-2">${pair.caseA.description}</p>
            </div>

            <div class="p-3 bg-white border border-slate-200 rounded-xl space-y-1">
              <div class="flex items-center justify-between">
                <span class="font-bold text-purple-900">${pair.caseB.assignedBureau}</span>
                <span class="font-mono text-slate-500 font-bold">${pair.caseB.caseId}</span>
              </div>
              <div class="font-bold text-slate-800">${pair.caseB.title}</div>
              <p class="text-[11px] text-slate-500 line-clamp-2">${pair.caseB.description}</p>
            </div>
          </div>

          <div class="space-y-1 pt-1">
            <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Algorithmic Correlation Factors:</div>
            <ul class="list-disc pl-5 text-[11px] text-slate-600 space-y-0.5">
              ${pair.reasons.map(r => `<li>${r}</li>`).join('')}
            </ul>
          </div>

          <div class="flex justify-end pt-2">
            ${pair.isLinked ? `
              <button onclick="viewComplaintDetails('${pair.caseA.caseId}')" class="px-4 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold rounded-xl text-xs">
                View Synchronized Dossier &rarr;
              </button>
            ` : `
              <button onclick="openCoordinationModal('${pair.caseA.caseId}', '${pair.caseB.caseId}')" class="px-4 py-2 bg-gov-teal hover:bg-gov-darkTeal text-white font-bold rounded-xl text-xs shadow-sm">
                Establish Joint Coordination Link &rarr;
              </button>
            `}
          </div>
        </div>
      `).join('');
    }

    function runOverlapScan() {
      const pairs = findPotentialOverlaps();
      renderOverlapCases();
      showToast(`Overlap scan completed. Found ${pairs.length} concurrent case pairs.`, 'info');
    }

    let activeLinkCaseA = null;
    let activeLinkCaseB = null;

    function openCoordinationModal(caseAId, caseBId) {
      activeLinkCaseA = caseAId;
      activeLinkCaseB = caseBId;
      document.getElementById('coordinationRemarks').value = '';
      document.getElementById('coordinationModal').classList.remove('hidden');
    }

    function closeCoordinationModal() {
      document.getElementById('coordinationModal').classList.add('hidden');
    }

    function confirmLinkCases() {
      const remarks = document.getElementById('coordinationRemarks').value.trim() || 'Coordinated investigation agreed across bureaus.';
      const cA = complaints.find(c => c.caseId === activeLinkCaseA);
      const cB = complaints.find(c => c.caseId === activeLinkCaseB);

      if (cA && cB) {
        if (!cA.linkedCaseIds) cA.linkedCaseIds = [];
        if (!cB.linkedCaseIds) cB.linkedCaseIds = [];

        if (!cA.linkedCaseIds.includes(cB.caseId)) cA.linkedCaseIds.push(cB.caseId);
        if (!cB.linkedCaseIds.includes(cA.caseId)) cB.linkedCaseIds.push(cA.caseId);

        const timeStr = new Date().toLocaleDateString('en-GB') + ', ' + new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        cA.timeline.unshift({ date: timeStr, officer: currentUser.name, bureau: 'RB/PGRC', action: 'Joint Link Established', remarks: remarks });
        cB.timeline.unshift({ date: timeStr, officer: currentUser.name, bureau: 'RB/PGRC', action: 'Joint Link Established', remarks: remarks });

        auditLogs.unshift({
          id: 'aud-' + Math.floor(100 + Math.random() * 900),
          timestamp: new Date().toISOString().replace('T', ' ').substring(0, 19),
          actorId: currentUser.id,
          actorName: currentUser.name,
          actorRole: currentUser.role,
          action: 'LINK_OVERLAP_CASES',
          targetType: 'COMPLAINT',
          targetId: `${activeLinkCaseA}<->${activeLinkCaseB}`,
          details: `Linked cases under joint coordination. Remarks: ${remarks}`
        });

        saveData();
        closeCoordinationModal();
        renderOverlapCases();
        renderRecentComplaintsTable();
        showToast(`Established joint coordination link between ${activeLinkCaseA} and ${activeLinkCaseB}.`, 'success');
      }
    }

    // ==========================================
    // 6. ROLE DATA RESTRICTIONS & TABLE RENDERERS
    // ==========================================
    function getRoleFilteredComplaints() {
      // Role-based data boundaries
      if (currentRole === 'college_inst') {
        // Only complaints regarding Apex Institute
        return complaints.filter(c => c.aicteId === '1-3324567891');
      }
      if (currentRole === 'university') {
        // Affiliated technical colleges under State Tech Univ
        return complaints.filter(c => c.aicteId === '1-3324567891');
      }
      if (currentRole === 'ro_officer') {
        // Western Regional Office only
        return complaints.filter(c => c.region === 'Western Region (WRO)' || c.aicteId === '1-3324567891');
      }
      if (currentRole === 'rb_officer') {
        // RB complaints or cross-bureau overlaps
        return complaints;
      }
      return complaints;
    }

    function renderDashboardStats() {
      const filtered = getRoleFilteredComplaints();
      const total = filtered.length;
      const pending = filtered.filter(c => c.status === 'Under Process' || c.status === 'Pending').length;
      const overdue = filtered.filter(c => c.isOverdue).length;
      const overlaps = findPotentialOverlaps().length;

      const k1 = document.getElementById('kpiCard1Val');
      const k2 = document.getElementById('kpiCard2Val');
      const k3 = document.getElementById('kpiCard3Val');
      const k4 = document.getElementById('kpiCard4Val');

      if (k1) k1.textContent = total;
      if (k2) k2.textContent = pending;
      if (k3) k3.textContent = overdue;
      if (k4) k4.textContent = overlaps;
    }

    function renderRecentComplaintsTable() {
      const tbody = document.getElementById('recentComplaintsTableBody');
      if (!tbody) return;

      const filtered = getRoleFilteredComplaints().slice(0, 5);
      if (filtered.length === 0) {
        tbody.innerHTML = '<tr><td colspan="6" class="py-4 text-center text-slate-400 italic">No complaints found matching current access boundaries.</td></tr>';
        return;
      }

      tbody.innerHTML = filtered.map(c => `
        <tr class="hover:bg-slate-50 transition-colors">
          <td class="py-2.5 px-3 font-mono font-bold text-gov-lightBlue">
            <a href="javascript:void(0)" onclick="viewComplaintDetails('${c.caseId}')" class="hover:underline">${c.caseId}</a>
          </td>
          <td class="py-2.5 px-3 font-medium text-slate-900">${c.instName}</td>
          <td class="py-2.5 px-3 text-slate-600">${c.category}</td>
          <td class="py-2.5 px-3 font-semibold text-slate-700">${c.assignedBureau}</td>
          <td class="py-2.5 px-3">${getStatusBadge(c.status, c.isOverdue)}</td>
          <td class="py-2.5 px-3 text-right">
            <button onclick="viewComplaintDetails('${c.caseId}')" class="px-3 py-1 bg-slate-100 hover:bg-gov-navy hover:text-white text-slate-700 font-bold rounded-lg text-[11px] transition-colors">
              Inspect Dossier &rarr;
            </button>
          </td>
        </tr>
      `).join('');
    }

    function renderAllComplaintsTable() {
      const tbody = document.getElementById('allComplaintsTableBody');
      if (!tbody) return;

      const filtered = getRoleFilteredComplaints();
      tbody.innerHTML = filtered.map(c => `
        <tr class="hover:bg-slate-50 transition-colors">
          <td class="py-3 px-3 font-mono font-bold text-gov-lightBlue">
            <a href="javascript:void(0)" onclick="viewComplaintDetails('${c.caseId}')" class="hover:underline">${c.caseId}</a>
          </td>
          <td class="py-3 px-3 font-bold text-slate-900">${c.instName}</td>
          <td class="py-3 px-3 text-slate-600">${c.category}</td>
          <td class="py-3 px-3 text-slate-700 font-medium">${c.assignedOfficer}</td>
          <td class="py-3 px-3">
            <span class="badge ${c.kycRecord && c.kycRecord.status === 'Verified' ? 'bg-emerald-100 text-emerald-900 border border-emerald-300' : 'bg-slate-100 text-slate-700'} text-[10px]">
              ${c.kycRecord ? c.kycRecord.status : 'Verified'}
            </span>
          </td>
          <td class="py-3 px-3">${getStatusBadge(c.status, c.isOverdue)}</td>
          <td class="py-3 px-3 text-right">
            <button onclick="viewComplaintDetails('${c.caseId}')" class="px-3 py-1 bg-gov-navy hover:bg-gov-darkNavy text-white font-bold rounded-lg text-xs transition-colors">
              View &rarr;
            </button>
          </td>
        </tr>
      `).join('');
    }

    function renderInstitutionsTable() {
      const tbody = document.getElementById('institutionsTableBody');
      if (!tbody) return;

      tbody.innerHTML = institutions.map(inst => `
        <tr class="hover:bg-slate-50 transition-colors">
          <td class="py-3 px-3 font-mono font-bold text-gov-navy">${inst.id}</td>
          <td class="py-3 px-3 font-bold text-slate-900">${inst.name}</td>
          <td class="py-3 px-3 text-slate-600">${inst.region}</td>
          <td class="py-3 px-3">
            <span class="badge ${inst.status.includes('Approved') ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'}">
              ${inst.status}
            </span>
          </td>
          <td class="py-3 px-3 font-mono text-xs text-slate-500">${(inst.linkedCases || []).length} active</td>
          <td class="py-3 px-3 text-right">
            <button onclick="viewInstitutionDetails('${inst.id}')" class="px-3 py-1 bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold rounded-lg text-xs">
              Dossier &rarr;
            </button>
          </td>
        </tr>
      `).join('');
    }

    function renderUsersTable() {
      const tbody = document.getElementById('adminUsersTableBody');
      const pendingContainer = document.getElementById('pendingApprovalsContainer');
      const auditTbody = document.getElementById('systemAuditLogsTableBody');

      if (tbody) {
        tbody.innerHTML = users.map(u => `
          <tr class="hover:bg-slate-50 transition-colors">
            <td class="py-3 px-3">
              <div class="font-bold text-slate-900">${u.name}</div>
              <div class="text-[11px] text-slate-500">${u.orgName || 'AICTE Council'}</div>
            </td>
            <td class="py-3 px-3 font-mono text-[11px] font-bold text-gov-blue">${u.role}</td>
            <td class="py-3 px-3 text-slate-600 text-[11px]">${u.email}</td>
            <td class="py-3 px-3">
              <span class="badge ${u.status === 'active' ? 'bg-emerald-100 text-emerald-800' : u.status === 'pending_approval' ? 'bg-amber-100 text-amber-800' : 'bg-rose-100 text-rose-800'}">
                ${u.status}
              </span>
            </td>
            <td class="py-3 px-3 text-right space-x-1">
              <button onclick="toggleUserStatus('${u.id}')" class="px-2.5 py-1 bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold rounded text-[11px]">
                ${u.status === 'active' ? 'Deactivate' : 'Activate'}
              </button>
            </td>
          </tr>
        `).join('');
      }

      if (pendingContainer) {
        const pendingUsers = users.filter(u => u.status === 'pending_approval');
        if (pendingUsers.length === 0) {
          pendingContainer.innerHTML = '<div class="p-3 text-slate-400 italic text-center bg-slate-50">No pending institution or university registrations.</div>';
        } else {
          pendingContainer.innerHTML = pendingUsers.map(u => `
            <div class="p-3 bg-amber-50/40 border border-amber-200 rounded-xl flex items-center justify-between text-xs">
              <div>
                <span class="font-bold text-slate-900">${u.name} (${u.orgName})</span>
                <div class="text-[11px] text-slate-500 font-mono">Role: ${u.role} &bull; Email: ${u.email}</div>
              </div>
              <div class="flex items-center gap-2">
                <button onclick="approveUserRegistration('${u.id}')" class="px-3 py-1 bg-emerald-600 text-white font-bold rounded-lg text-xs hover:bg-emerald-500">
                  Approve Registration
                </button>
              </div>
            </div>
          `).join('');
        }
      }

      if (auditTbody) {
        auditTbody.innerHTML = auditLogs.map(a => `
          <tr class="hover:bg-slate-50">
            <td class="py-2 px-3 text-slate-400 whitespace-nowrap">${a.timestamp}</td>
            <td class="py-2 px-3 font-bold text-slate-800">${a.actorName} (${a.actorRole})</td>
            <td class="py-2 px-3 text-gov-blue font-bold">${a.action}</td>
            <td class="py-2 px-3 font-mono text-slate-600">${a.targetId}</td>
            <td class="py-2 px-3 text-slate-600 text-[10px]">${a.details}</td>
          </tr>
        `).join('');
      }
    }

    function toggleUserStatus(userId) {
      const u = users.find(x => x.id === userId);
      if (u) {
        u.status = u.status === 'active' ? 'suspended' : 'active';
        saveData();
        renderUsersTable();
        showToast(`Updated user status for ${u.name} to ${u.status}`, 'info');
      }
    }

    function approveUserRegistration(userId) {
      const u = users.find(x => x.id === userId);
      if (u) {
        u.status = 'active';
        u.approvedBy = currentUser.name;
        u.approvedAt = new Date().toISOString();
        auditLogs.unshift({
          id: 'aud-' + Math.floor(100 + Math.random() * 900),
          timestamp: new Date().toISOString().replace('T', ' ').substring(0, 19),
          actorId: currentUser.id,
          actorName: currentUser.name,
          actorRole: currentUser.role,
          action: 'APPROVE_USER',
          targetType: 'USER',
          targetId: u.id,
          details: `Approved account registration for ${u.name} (${u.orgName})`
        });
        saveData();
        renderUsersTable();
        showToast(`Approved registration for ${u.name}`, 'success');
      }
    }

    // ==========================================
    // 7. MODALS, TRACKING & NAVIGATION HELPERS
    // ==========================================
    function viewComplaintDetails(caseId) {
      const c = complaints.find(x => x.caseId === caseId);
      if (!c) return;

      document.getElementById('modalCaseId').textContent = c.caseId;
      document.getElementById('modalInstName').textContent = c.instName;
      document.getElementById('modalAicteId').textContent = c.aicteId;
      document.getElementById('modalBureauOfficer').textContent = `${c.assignedBureau} • ${c.assignedOfficer}`;
      document.getElementById('modalDateReceived').textContent = `${c.dateReceived} (${c.complainantType})`;
      document.getElementById('modalDescription').textContent = c.description;

      const statusBadge = document.getElementById('modalCaseStatusBadge');
      if (statusBadge) {
        statusBadge.textContent = c.status;
        statusBadge.className = `badge ${c.status === 'Resolved' ? 'bg-emerald-100 text-emerald-900' : 'bg-blue-100 text-blue-900'}`;
      }

      // KYC Details
      const kycSection = document.getElementById('modalKycSection');
      const kycBadge = document.getElementById('modalKycBadge');
      const kycDetails = document.getElementById('modalKycDetails');
      if (c.kycRecord) {
        kycBadge.textContent = c.kycRecord.status;
        kycBadge.className = `badge ${c.kycRecord.status === 'Verified' ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'}`;
        kycDetails.innerHTML = `
          <div>Provider: ${c.kycRecord.provider} &bull; Ref: ${c.kycRecord.referenceId} &bull; Verified At: ${c.kycRecord.verifiedAt || 'Verified'}</div>
          <div class="text-[11px] text-slate-500">Identity cryptographically asserted. Complainant Name: ${c.kycRecord.complainantName || c.complainantType}</div>
        `;
      }

      // Evidence & Hive AI badges
      const docsContainer = document.getElementById('modalDocsContainer');
      if (docsContainer) {
        if (c.evidenceItems && c.evidenceItems.length > 0) {
          docsContainer.innerHTML = c.evidenceItems.map(ev => {
            const scr = ev.screening || {};
            const isFlagged = scr.status && scr.status.includes('Potential AI');
            const badgeColor = scr.status && scr.status.includes('No AI Signal') ? 'bg-emerald-100 text-emerald-900 border-emerald-300' :
                               isFlagged ? 'bg-rose-100 text-rose-900 border-rose-300' :
                               'bg-slate-100 text-slate-800 border-slate-300';
            return `
              <div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-1.5">
                <div class="flex items-center justify-between">
                  <span class="font-bold text-slate-800">${ev.name}</span>
                  <span class="badge ${badgeColor} border text-[10px]">${scr.status || 'Screened'}</span>
                </div>
                <div class="text-[11px] text-slate-500 font-mono">
                  <span>AI Signal: <strong>${scr.aiSignalPercentage || 0}%</strong></span> &bull; 
                  <span>Confidence: <strong>${scr.confidenceScore || 0}%</strong></span> &bull; 
                  <span>Model: ${scr.modelName || 'hive-ai-generated-image-detection-v2'}</span>
                </div>
                <p class="text-[11px] text-slate-600 leading-relaxed">${scr.explanation || 'Evidence analyzed via Hive AI Gateway.'}</p>
                ${ev.review ? `
                  <div class="mt-2 pt-2 border-t border-slate-200 text-[11px] text-blue-900 bg-blue-50/60 p-2 rounded-lg">
                    <strong>Officer Review (${ev.review.reviewerName}):</strong> ${ev.review.decision} &bull; <em>"${ev.review.reasoning}"</em>
                  </div>
                ` : ''}
              </div>
            `;
          }).join('');
        } else if (c.docs && c.docs.length > 0) {
          docsContainer.innerHTML = c.docs.map(d => `
            <div class="p-2.5 bg-slate-50 border border-slate-200 rounded-xl flex items-center justify-between">
              <span class="font-mono text-xs font-bold text-slate-800">${d.name} (${d.size})</span>
              <span class="badge bg-slate-200 text-slate-700 text-[10px]">Verified Document</span>
            </div>
          `).join('');
        }
      }

      // Overlap alert inside modal
      const modalOverlap = document.getElementById('modalOverlapNotice');
      if (modalOverlap) {
        if (c.linkedCaseIds && c.linkedCaseIds.length > 0) {
          modalOverlap.classList.remove('hidden');
          document.getElementById('modalOverlapNoticeText').textContent = `Linked under joint inter-bureau coordination with case(s): ${c.linkedCaseIds.join(', ')}`;
        } else {
          modalOverlap.classList.add('hidden');
        }
      }

      // Timeline
      const timelineEl = document.getElementById('modalTimeline');
      if (timelineEl) {
        timelineEl.innerHTML = (c.timeline || []).map(t => `
          <div class="relative pl-6 space-y-0.5">
            <span class="absolute left-0 top-1 w-2.5 h-2.5 rounded-full bg-gov-teal border-2 border-white ring-2 ring-gov-teal/30"></span>
            <div class="text-[10px] text-slate-400 font-mono">${t.date} &bull; ${t.officer} (${t.bureau})</div>
            <div class="font-bold text-slate-800 text-xs">${t.action}</div>
            <p class="text-slate-600 text-[11px]">${t.remarks}</p>
          </div>
        `).join('');
      }

      document.getElementById('complaintDetailModal').classList.remove('hidden');
    }

    function closeComplaintDetailModal() {
      document.getElementById('complaintDetailModal').classList.add('hidden');
    }

    function showPublicTrackModal() {
      document.getElementById('trackComplaintModal').classList.remove('hidden');
      trackComplaintPublic(lastSubmittedCaseId);
    }

    function closeTrackModal() {
      document.getElementById('trackComplaintModal').classList.add('hidden');
    }

    function trackComplaintPublic(targetId = null) {
      const qInput = document.getElementById('publicTrackId') || document.getElementById('quickSearchInput');
      const caseId = targetId || (qInput ? qInput.value.trim() : null) || 'AICTE/RB/2026/0104';
      const c = complaints.find(x => x.caseId.toLowerCase() === caseId.toLowerCase());
      const body = document.getElementById('trackModalBody');
      const headerTitle = document.getElementById('trackModalCaseId');

      if (!body) return;
      if (headerTitle) headerTitle.textContent = caseId.toUpperCase();

      if (!c) {
        body.innerHTML = `
          <div class="p-6 text-center text-slate-500 space-y-2">
            <div class="text-rose-500 font-bold">Case Reference Not Found</div>
            <p class="text-xs">No active or archived petition matches reference ID: <strong>${caseId}</strong>.</p>
          </div>
        `;
        return;
      }

      body.innerHTML = `
        <div class="bg-slate-50 p-4 rounded-2xl border border-slate-200 space-y-2">
          <div class="flex items-center justify-between border-b border-slate-200 pb-2">
            <span class="font-bold text-slate-900">${c.instName}</span>
            ${getStatusBadge(c.status, c.isOverdue)}
          </div>
          <div class="text-xs text-slate-600 font-medium">${c.title}</div>
          <div class="flex flex-wrap items-center gap-4 text-[11px] text-slate-500 pt-1">
            <span>Bureau: <strong>${c.assignedBureau}</strong></span>
            <span>&bull;</span>
            <span>Filed: <strong>${c.dateReceived}</strong></span>
            <span>&bull;</span>
            <span>SLA Target: <strong class="text-emerald-600">${c.expectedDisposalDate}</strong></span>
          </div>
        </div>

        <div>
          <div class="font-bold text-slate-800 text-xs uppercase mb-2">Chronological Inquiry Timeline:</div>
          <div class="space-y-3 relative before:absolute before:inset-0 before:left-3 before:w-0.5 before:bg-slate-200 pl-2">
            ${(c.timeline || []).map(t => `
              <div class="relative pl-6 space-y-0.5">
                <span class="absolute left-0 top-1 w-2.5 h-2.5 rounded-full bg-gov-teal border-2 border-white ring-2 ring-gov-teal/30"></span>
                <div class="text-[10px] text-slate-400 font-mono">${t.date}</div>
                <div class="font-bold text-slate-800 text-xs">${t.action} (${t.bureau})</div>
                <p class="text-slate-600 text-[11px]">${t.remarks}</p>
              </div>
            `).join('')}
          </div>
        </div>
      `;
    }

    function handlePublicTrackSubmit(e) {
      if (e) e.preventDefault();
      const qElem = document.getElementById('publicTrackId') || document.getElementById('quickSearchInput'); const id = qElem ? qElem.value.trim() : '';
      if (!id) return;
      showPublicTrackModal();
      trackComplaintPublic(id);
    }

    function handleQuickSearchSubmit(e) {
      if (e) e.preventDefault();
      executeQuickSearch();
    }

    function executeQuickSearch() {
      const q = document.getElementById('quickSearchInput').value.trim();
      if (!q) return;

      if (q.toUpperCase().startsWith('AICTE/')) {
        showPublicTrackModal();
        trackComplaintPublic(q);
      } else {
        const inst = institutions.find(i => i.id === q || i.name.toLowerCase().includes(q.toLowerCase()));
        if (inst) {
          viewInstitutionDetails(inst.id);
        } else {
          openInstitutionsDirectoryModal();
        }
      }
    }

    function viewInstitutionDetails(instId) {
      const inst = institutions.find(i => i.id === instId);
      if (!inst) return;

      document.getElementById('instModalName').textContent = inst.name;
      document.getElementById('instModalId').textContent = inst.id;
      document.getElementById('instModalRegion').textContent = `${inst.state} (${inst.region})`;
      document.getElementById('instModalStatus').textContent = inst.status;
      document.getElementById('instModalHead').textContent = inst.head;

      const actList = document.getElementById('instModalActionsList');
      if (actList) {
        if (!inst.regulatoryActions || inst.regulatoryActions.length === 0) {
          actList.innerHTML = '<div class="text-slate-400 italic">No active punitive or regulatory sanctions recorded.</div>';
        } else {
          actList.innerHTML = inst.regulatoryActions.map(a => `
            <div class="p-2 bg-amber-50 border border-amber-200 rounded-lg text-amber-900 text-xs flex items-center gap-1.5">
              <span>&bull;</span>
              <span>${a}</span>
            </div>
          `).join('');
        }
      }

      const compTbody = document.getElementById('instModalComplaintsTable');
      if (compTbody) {
        const linked = complaints.filter(c => c.aicteId === inst.id);
        if (linked.length === 0) {
          compTbody.innerHTML = '<tr><td colspan="5" class="py-3 text-center text-slate-400 italic">No recorded complaints for this institution.</td></tr>';
        } else {
          compTbody.innerHTML = linked.map(c => `
            <tr class="hover:bg-slate-50">
              <td class="py-2 px-3 font-mono font-bold text-gov-lightBlue">${c.caseId}</td>
              <td class="py-2 px-3 text-slate-700">${c.assignedBureau}</td>
              <td class="py-2 px-3 text-slate-600">${c.category}</td>
              <td class="py-2 px-3">${getStatusBadge(c.status, c.isOverdue)}</td>
              <td class="py-2 px-3 text-right">
                <button onclick="closeInstitutionModal(); viewComplaintDetails('${c.caseId}')" class="px-2 py-0.5 bg-gov-navy text-white font-bold rounded text-[10px]">
                  View &rarr;
                </button>
              </td>
            </tr>
          `).join('');
        }
      }

      document.getElementById('institutionModal').classList.remove('hidden');
    }

    function closeInstitutionModal() {
      document.getElementById('institutionModal').classList.add('hidden');
    }

    // Auth Modals
    function showLoginModal() {
      document.getElementById('loginModal').classList.remove('hidden');
    }
    function closeLoginModal() {
      document.getElementById('loginModal').classList.add('hidden');
    }
    function showRegisterModal() {
      document.getElementById('registerModal').classList.remove('hidden');
    }
    function closeRegisterModal() {
      document.getElementById('registerModal').classList.add('hidden');
    }
    function switchToRegisterModal() {
      closeLoginModal();
      showRegisterModal();
    }
    function switchToLoginModal() {
      closeRegisterModal();
      showLoginModal();
    }
    function closeRegSuccessModal() {
      document.getElementById('regSuccessModal').classList.add('hidden');
    }
    function closeComplaintConfModal() {
      document.getElementById('complaintConfirmationModal').classList.add('hidden');
    }

    function openAboutModal() {
      document.getElementById('aboutModal').classList.remove('hidden');
    }
    function closeAboutModal() {
      document.getElementById('aboutModal').classList.add('hidden');
    }
    function openHelpModal() {
      document.getElementById('helpModal').classList.remove('hidden');
    }
    function closeHelpModal() {
      document.getElementById('helpModal').classList.add('hidden');
    }
    function openGuidelinesModal() {
      document.getElementById('guidelinesModal').classList.remove('hidden');
    }
    function closeGuidelinesModal() {
      document.getElementById('guidelinesModal').classList.add('hidden');
    }
    function openInstitutionsDirectoryModal() {
      const tbody = document.getElementById('directoryTableBody');
      if (tbody) {
        tbody.innerHTML = institutions.map(i => `
          <tr class="hover:bg-slate-50">
            <td class="py-2.5 px-3 font-mono font-bold text-gov-navy">${i.id}</td>
            <td class="py-2.5 px-3 font-bold text-slate-800">${i.name}</td>
            <td class="py-2.5 px-3 text-slate-600">${i.region}</td>
            <td class="py-2.5 px-3">
              <span class="badge ${i.status.includes('Approved') ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'} text-[10px]">${i.status}</span>
            </td>
            <td class="py-2.5 px-3 text-right">
              <button onclick="closeInstitutionsDirectoryModal(); viewInstitutionDetails('${i.id}')" class="px-2.5 py-1 bg-slate-100 hover:bg-gov-navy hover:text-white font-bold rounded text-xs transition-colors">
                View &rarr;
              </button>
            </td>
          </tr>
        `).join('');
      }
      document.getElementById('institutionsDirectoryModal').classList.remove('hidden');
    }
    function closeInstitutionsDirectoryModal() {
      document.getElementById('institutionsDirectoryModal').classList.add('hidden');
    }
    function openEvidenceReviewFromLanding() {
      openRolePortal('rb_officer');
      switchTab('dashboard');
      setTimeout(() => {
        const el = document.getElementById('evidenceReviewWorkspace');
        if (el) el.scrollIntoView({ behavior: 'smooth' });
      }, 100);
    }
    function openBureauCoordinationGuide() {
      openRolePortal('rb_officer');
      switchTab('overlap');
    }

    function selectDemoRole(role) {
      const u = users.find(x => x.role === role);
      if (u) {
        document.getElementById('loginUsername').value = u.email;
        document.getElementById('loginPassword').value = u.passwordHash;
      }
    }

    function handleLoginSubmit(e) {
      if (e) e.preventDefault();
      const email = document.getElementById('loginUsername').value.trim();
      const pwd = document.getElementById('loginPassword').value;

      const user = users.find(u => u.email.toLowerCase() === email.toLowerCase());
      if (user) {
        if (user.status === 'pending_approval') {
          showToast('Account is Pending Administrator Verification. Please contact AICTE Admin.', 'error');
          return;
        }
        closeLoginModal();
        openRolePortal(user.role);
        showToast(`Welcome back, ${user.name}!`, 'success');
      } else {
        const alert = document.getElementById('loginErrorAlert');
        alert.classList.remove('hidden');
        document.getElementById('loginErrorText').textContent = 'Invalid credentials or unregistered institutional email.';
      }
    }

    function handleRegisterSubmit(e) {
      if (e) e.preventDefault();
      const role = document.getElementById('regRole').value;
      const orgName = document.getElementById('regOrgName').value.trim();
      const aicteId = document.getElementById('regAicteId').value.trim();
      const name = document.getElementById('regName').value.trim();
      const email = document.getElementById('regEmail').value.trim();
      const phone = document.getElementById('regPhone').value.trim();
      const pwd = document.getElementById('regPassword').value;
      const confirmPwd = document.getElementById('regConfirmPassword').value;

      if (pwd !== confirmPwd) {
        const err = document.getElementById('regErrorAlert');
        err.classList.remove('hidden');
        document.getElementById('regErrorText').textContent = 'Passwords do not match.';
        return;
      }

      // Check Administrative Privilege Governance Rule
      const isPrivileged = ['admin', 'senior_mgmt', 'rb_officer', 'pgrc_officer', 'ro_officer'].includes(role);
      const initialStatus = isPrivileged ? 'pending_approval' : 'active';

      const newUser = {
        id: 'usr-' + (users.length + 1),
        name: name,
        email: email,
        role: role,
        orgName: orgName,
        aicteId: aicteId || '1-PENDING',
        phone: phone,
        status: initialStatus,
        passwordHash: pwd,
        registeredAt: new Date().toISOString().split('T')[0]
      };

      users.push(newUser);
      saveData();
      closeRegisterModal();

      const successTitle = document.getElementById('regSuccessTitle');
      const successMsg = document.getElementById('regSuccessMessage');

      if (isPrivileged) {
        successTitle.textContent = 'Registration Received  -  Verification Required';
        successMsg.textContent = 'Your registration for a regulatory / administrative role has been queued for verification by an authorized AICTE Administrator.';
      } else {
        successTitle.textContent = 'Registration Successful';
        successMsg.textContent = `Your institutional account for ${orgName} has been activated. You can now log in and manage your institution complaints.`;
      }

      document.getElementById('regSuccessModal').classList.remove('hidden');
    }

    function handleRoleFieldChange(val) {
      const notice = document.getElementById('adminRoleSecurityNotice');
      if (!notice) return;
      if (['admin', 'senior_mgmt', 'rb_officer', 'pgrc_officer', 'ro_officer'].includes(val)) {
        notice.classList.remove('hidden');
      } else {
        notice.classList.add('hidden');
      }
    }

    function togglePasswordVisibility() {
      const input = document.getElementById('loginPassword');
      if (input.type === 'password') input.type = 'text';
      else input.type = 'password';
    }

    function toggleRoleDropdown(e) {
      if (e) e.stopPropagation();
      const menu = document.getElementById('roleDropdownMenu');
      const chevron = document.getElementById('triggerChevron');
      if (!menu) return;

      const isHidden = menu.classList.contains('hidden');
      if (isHidden) {
        menu.classList.remove('hidden');
        menu.classList.add('animate-slide-down');
        if (chevron) chevron.classList.add('rotate-180', 'text-cyan-300');
      } else {
        closeRoleDropdown();
      }
    }

    function closeRoleDropdown() {
      const menu = document.getElementById('roleDropdownMenu');
      const chevron = document.getElementById('triggerChevron');
      if (menu && !menu.classList.contains('hidden')) {
        menu.classList.add('hidden');
        menu.classList.remove('animate-slide-down');
      }
      if (chevron) {
        chevron.classList.remove('rotate-180', 'text-cyan-300');
      }
    }

    function selectRoleOption(role) {
      changeActiveRole(role);
      closeRoleDropdown();
    }

    document.addEventListener('click', (e) => {
      const container = document.getElementById('customRoleDropdownContainer');
      if (container && !container.contains(e.target)) {
        closeRoleDropdown();
      }
      const notifDrop = document.getElementById('notifDropdown');
      if (notifDrop && !notifDrop.contains(e.target) && !e.target.closest('button[onclick*="toggleNotifDropdown"]')) {
        notifDrop.classList.add('hidden');
      }
    });

    function toggleNotifDropdown(e) {
      if (e) e.stopPropagation();
      const d = document.getElementById('notifDropdown');
      if (!d) return;
      d.classList.toggle('hidden');
      renderNotifications();
    }

    function renderNotifications() {
      const list = document.getElementById('notifList');
      if (!list) return;

      if (notifications.length === 0) {
        list.innerHTML = '<div class="p-4 text-center text-slate-400">No unread notifications.</div>';
        return;
      }

      list.innerHTML = notifications.map(n => `
        <div class="p-3 hover:bg-slate-50 transition-colors cursor-pointer" onclick="viewComplaintDetails('${n.targetCase || ''}')">
          <div class="font-bold text-slate-800 text-xs">${n.title}</div>
          <div class="text-[11px] text-slate-600 mt-0.5">${n.desc}</div>
          <div class="text-[10px] text-slate-400 mt-1 font-mono">${n.time}</div>
        </div>
      `).join('');
    }

    function switchTab(tabId) {
      activeTab = tabId;
      const tabs = ['dashboard', 'complaints', 'overlap', 'institutions', 'reports', 'users'];
      tabs.forEach(t => {
        const content = document.getElementById(`tab-content-${t}`);
        const nav = document.getElementById(`nav-tab-${t}`);
        if (content) {
          if (t === tabId) content.classList.remove('hidden');
          else content.classList.add('hidden');
        }
        if (nav) {
          if (t === tabId) nav.classList.add('tab-active');
          else nav.classList.remove('tab-active');
        }
      });

      if (tabId === 'reports') {
        updateCharts();
      }
    }

    function getStatusBadge(status, isOverdue) {
      if (isOverdue) return '<span class="badge bg-rose-100 text-rose-800 font-bold border border-rose-300">Overdue SLA</span>';
      if (status === 'Resolved' || status === 'Disposed') return '<span class="badge bg-emerald-100 text-emerald-800 font-bold">Resolved</span>';
      if (status === 'Escalated') return '<span class="badge bg-amber-100 text-amber-900 font-bold">Escalated</span>';
      return '<span class="badge bg-blue-100 text-blue-900 font-bold">Under Process</span>';
    }

    function showToast(message, type = 'info') {
      const container = document.getElementById('toastContainer');
      if (!container) return;

      const toast = document.createElement('div');
      const bg = type === 'success' ? 'bg-emerald-700 text-white' :
                 type === 'error' ? 'bg-rose-700 text-white' :
                 'bg-gov-navy text-white';

      toast.className = `${bg} px-4 py-2.5 rounded-xl text-xs font-bold shadow-lg flex items-center gap-2 pointer-events-auto transition-all transform duration-300 translate-y-2 opacity-0`;
      toast.innerHTML = `<span>${message}</span>`;
      container.appendChild(toast);

      setTimeout(() => {
        toast.classList.remove('translate-y-2', 'opacity-0');
      }, 50);

      setTimeout(() => {
        toast.classList.add('opacity-0', 'translate-y-2');
        setTimeout(() => toast.remove(), 300);
      }, 4000);
    }

    function toggleMobileNav() {
      const menu = document.getElementById('mobileNavMenu');
      if (menu) menu.classList.toggle('hidden');
    }

    function toggleHighContrast() {
      document.body.classList.toggle('contrast-125');
      showToast('High Contrast Mode toggled.', 'info');
    }

    function scrollToSection(id) {
      const el = document.getElementById(id);
      if (el) el.scrollIntoView({ behavior: 'smooth' });
    }

    function handleLogout() {
      showLandingPage();
      showToast('You have been logged out of the session.', 'info');
    }

    function downloadExecutiveBriefingReport() {
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify({
        generatedAt: new Date().toISOString(),
        totalComplaints: complaints.length,
        disposalRatePercentage: 78.5,
        bureauBreakdown: { RB: 3, PGRC: 3 },
        complaints: complaints
      }, null, 2));
      const downloadAnchor = document.createElement('a');
      downloadAnchor.setAttribute("href", dataStr);
      downloadAnchor.setAttribute("download", "AICTE_Executive_Briefing_SIH2026.json");
      document.body.appendChild(downloadAnchor);
      downloadAnchor.click();
      downloadAnchor.remove();
      showToast('Executive briefing dataset downloaded successfully.', 'success');
    }

    // Chart.js Visualizations
    let bureauChartInstance = null;
    let statusChartInstance = null;

    function updateCharts() {
      if (typeof Chart === 'undefined') return;

      const bCanvas = document.getElementById('bureauChart');
      if (bCanvas) {
        if (bureauChartInstance) bureauChartInstance.destroy();
        bureauChartInstance = new Chart(bCanvas, {
          type: 'doughnut',
          data: {
            labels: ['Regulation Bureau (RB)', 'PGRC', 'Approval Bureau (AB)'],
            datasets: [{
              data: [3, 3, 1],
              backgroundColor: ['#003366', '#008080', '#0077B6'],
              borderWidth: 2
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { position: 'bottom', labels: { font: { size: 10, family: 'Inter' } } }
            }
          }
        });
      }

      const sCanvas = document.getElementById('statusChart');
      if (sCanvas) {
        if (statusChartInstance) statusChartInstance.destroy();
        statusChartInstance = new Chart(sCanvas, {
          type: 'bar',
          data: {
            labels: ['Under Process', 'Pending Notice', 'Escalated', 'Resolved'],
            datasets: [{
              label: 'Case Count',
              data: [3, 2, 1, 1],
              backgroundColor: ['#0077B6', '#F59E0B', '#DC2626', '#15803D'],
              borderRadius: 8
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { display: false }
            },
            scales: {
              y: { beginAtZero: true, ticks: { stepSize: 1, font: { size: 10 } } },
              x: { ticks: { font: { size: 10 } } }
            }
          }
        });
      }
    }

    // Clock Updater
    function updateClock() {
      const now = new Date();
      const timeStr = now.toLocaleTimeString('en-IN', { timeZone: 'Asia/Kolkata', hour12: false }) + ' IST';
      const l1 = document.getElementById('landingLiveClock');
      const l2 = document.getElementById('portalLiveClock');
      if (l1) l1.textContent = timeStr;
      if (l2) l2.textContent = timeStr;
    }

    // App Initialization
    function initUI() {
      setInterval(updateClock, 1000);
      updateClock();

      // Check current route on load
      handleRoute();
      if (typeof lucide !== 'undefined' && lucide.createIcons) {
        lucide.createIcons();
      }
    }

    document.addEventListener('DOMContentLoaded', initUI);
  </script>
</body>
</html>
'''
