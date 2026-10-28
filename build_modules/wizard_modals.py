# -*- coding: utf-8 -*-
"""
Wizard and Modal definitions for AICTE Complaint Monitoring System.
Includes:
- 6-Step Complaint Submission Wizard (/raise-complaint) with Mandatory KYC & Hive AI Screening
- Login Modal with 1-click evaluation roles
- Registration Modal with 7 roles & Administrative Privilege Governance Rule
- Case Detail Modal with Evidence Dossier & Officer Review Panel
- Case Tracking Modal (/track)
- Inter-Bureau Joint Coordination Modal
- Helper Modals (About, Help, Guidelines, Directory)
"""

def get_wizard_and_modals_html():
    return '''  <!-- ========================================== -->
  <!-- 2. 6-STEP COMPLAINT SUBMISSION WIZARD MODAL (/raise-complaint) -->
  <!-- ========================================== -->
  <div id="wizardModal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-3 sm:p-4 overflow-y-auto">
    <div class="max-w-3xl w-full bg-white rounded-3xl shadow-2xl border border-slate-200 overflow-hidden my-auto flex flex-col max-h-[94vh]">
      
      <!-- Wizard Top Header with Steps Indicator -->
      <div class="bg-gov-navy text-white px-6 py-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3 shrink-0">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-amber-400 text-slate-950 flex items-center justify-center font-black text-sm">
            AICTE
          </div>
          <div>
            <h3 class="text-base font-extrabold tracking-tight">AICTE Grievance Petition Wizard</h3>
            <p class="text-xs text-cyan-200">Mandatory KYC Verification &bull; Hive AI Evidence Screening</p>
          </div>
        </div>
        <div class="flex items-center gap-3 self-end sm:self-center">
          <button type="button" onclick="saveWizardDraft()" class="text-xs bg-blue-900 hover:bg-blue-800 text-cyan-200 px-3 py-1.5 rounded-lg border border-cyan-400/40 font-bold flex items-center gap-1">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"></path></svg>
            <span>Save Draft</span>
          </button>
          <button onclick="closeComplaintWizard()" class="text-slate-400 hover:text-white text-xl font-bold">&times;</button>
        </div>
      </div>

      <!-- Steps Progress Bar -->
      <div class="bg-slate-100 border-b border-slate-200 px-6 py-2.5 flex items-center justify-between text-[11px] font-bold overflow-x-auto shrink-0">
        <div id="wizStepTab1" class="flex items-center gap-1.5 text-gov-navy">
          <span class="w-5 h-5 rounded-full bg-gov-navy text-white flex items-center justify-center text-[10px]">1</span>
          <span>Complainant</span>
        </div>
        <span class="text-slate-300">&rarr;</span>
        <div id="wizStepTab2" class="flex items-center gap-1.5 text-slate-400">
          <span class="w-5 h-5 rounded-full bg-slate-300 text-white flex items-center justify-center text-[10px]">2</span>
          <span>KYC Verification</span>
        </div>
        <span class="text-slate-300">&rarr;</span>
        <div id="wizStepTab3" class="flex items-center gap-1.5 text-slate-400">
          <span class="w-5 h-5 rounded-full bg-slate-300 text-white flex items-center justify-center text-[10px]">3</span>
          <span>Complaint</span>
        </div>
        <span class="text-slate-300">&rarr;</span>
        <div id="wizStepTab4" class="flex items-center gap-1.5 text-slate-400">
          <span class="w-5 h-5 rounded-full bg-slate-300 text-white flex items-center justify-center text-[10px]">4</span>
          <span>Evidence</span>
        </div>
        <span class="text-slate-300">&rarr;</span>
        <div id="wizStepTab5" class="flex items-center gap-1.5 text-slate-400">
          <span class="w-5 h-5 rounded-full bg-slate-300 text-white flex items-center justify-center text-[10px]">5</span>
          <span>Hive AI</span>
        </div>
        <span class="text-slate-300">&rarr;</span>
        <div id="wizStepTab6" class="flex items-center gap-1.5 text-slate-400">
          <span class="w-5 h-5 rounded-full bg-slate-300 text-white flex items-center justify-center text-[10px]">6</span>
          <span>Submit</span>
        </div>
      </div>

      <!-- Wizard Body Container -->
      <div class="p-6 overflow-y-auto flex-1 space-y-4 text-xs text-slate-700">
        
        <!-- STEP 1: Complainant Details -->
        <div id="wizardStep1" class="space-y-4">
          <div class="border-b border-slate-200 pb-2">
            <h4 class="text-sm font-extrabold text-gov-navy">Step 1: Complainant Information &amp; Category</h4>
            <p class="text-xs text-slate-500">Collect only necessary details under AICTE Data Privacy and Whistleblower Protection guidelines.</p>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block font-bold text-slate-700 mb-1">Full Legal Name *</label>
              <input type="text" id="wizCompName" required placeholder="e.g. Prof. Rajesh K. Sharma / Rahul Verma" class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-slate-800 focus:outline-none focus:border-gov-teal">
            </div>
            <div>
              <label class="block font-bold text-slate-700 mb-1">Complainant Category *</label>
              <select id="wizCompType" required class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-slate-800 focus:outline-none focus:border-gov-teal">
                <option value="Faculty Member">Faculty Member (Teaching Staff)</option>
                <option value="Student / Parent">Student / Parent (Aggrieved Party)</option>
                <option value="Whistleblower">Whistleblower (Protected Identity)</option>
                <option value="Anonymous">Anonymous / Confidential Informant</option>
              </select>
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block font-bold text-slate-700 mb-1">Official / Personal Email Address *</label>
              <input type="email" id="wizCompEmail" required placeholder="name@domain.com" class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-slate-800 focus:outline-none focus:border-gov-teal">
            </div>
            <div>
              <label class="block font-bold text-slate-700 mb-1">Mobile Number (For OTP Verification) *</label>
              <input type="tel" id="wizCompPhone" required placeholder="+91 98765 43210" class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-slate-800 focus:outline-none focus:border-gov-teal">
            </div>
          </div>

          <div class="bg-blue-50 border border-blue-200 p-3 rounded-xl text-[11px] text-blue-900 flex items-start gap-2">
            <svg class="w-4 h-4 text-gov-lightBlue shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            <div>
              <strong>Privacy Protection Notice:</strong> Your identity will be masked for anonymous and whistleblower filings under AICTE Whistleblower Protection Norms. Identity details are securely retained only for genuine verification purposes.
            </div>
          </div>

          <div class="flex items-start gap-2 pt-1 text-[11px] text-slate-600">
            <input type="checkbox" id="wizConsentCheck" required class="rounded border-slate-300 text-gov-teal focus:ring-gov-teal mt-0.5">
            <label for="wizConsentCheck">
              I acknowledge that I am submitting this petition with truthful information and consent to necessary KYC verification.
            </label>
          </div>
        </div>

        <!-- STEP 2: Mandatory KYC Verification -->
        <div id="wizardStep2" class="hidden space-y-4">
          <div class="border-b border-slate-200 pb-2 flex items-center justify-between">
            <div>
              <h4 class="text-sm font-extrabold text-gov-navy">Step 2: Complainant KYC Verification</h4>
              <p class="text-xs text-slate-500">Section 5 Compliance: Mandatory identity verification before final submission.</p>
            </div>
            <div id="kycStatusBadge" class="badge bg-slate-100 text-slate-700 border border-slate-300">
              Not Started
            </div>
          </div>

          <div class="bg-slate-50 border border-slate-200 rounded-2xl p-4 space-y-3">
            <div class="text-xs font-bold text-slate-800">Select Authorized Verification Provider:</div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
              <label class="border border-slate-300 rounded-xl p-3 bg-white flex items-start gap-2 cursor-pointer hover:border-gov-teal">
                <input type="radio" name="kycProviderRadio" value="DigiLocker Sandbox" checked class="mt-0.5 text-gov-teal">
                <div>
                  <div class="font-bold text-slate-900">DigiLocker Sandbox (Gov of India)</div>
                  <div class="text-[11px] text-slate-500 mt-0.5">Cryptographic verification using digital student/faculty credential.</div>
                </div>
              </label>
              <label class="border border-slate-300 rounded-xl p-3 bg-white flex items-start gap-2 cursor-pointer hover:border-gov-teal">
                <input type="radio" name="kycProviderRadio" value="Gov Aadhaar e-KYC" class="mt-0.5 text-gov-teal">
                <div>
                  <div class="font-bold text-slate-900">Aadhaar e-KYC Simulation (UIDAI)</div>
                  <div class="text-[11px] text-slate-500 mt-0.5">Simulated OTP exchange via Government Identity Sandbox.</div>
                </div>
              </label>
            </div>

            <!-- KYC Action Container -->
            <div class="pt-2 flex flex-col sm:flex-row items-center justify-between gap-3">
              <div class="text-[11px] text-slate-500">
                Initiate verification code to confirm phone / email ownership.
              </div>
              <button type="button" id="btnInitiateKyc" onclick="initiateKycVerification()" class="px-4 py-2 bg-gov-lightBlue hover:bg-blue-600 text-white font-bold rounded-xl text-xs flex items-center gap-1.5 shrink-0">
                <svg class="w-4 h-4 text-cyan-200" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z"></path></svg>
                <span>Send Verification OTP</span>
              </button>
            </div>

            <!-- OTP Input Box (Revealed when pending) -->
            <div id="kycOtpContainer" class="hidden pt-3 border-t border-slate-200 space-y-3">
              <div class="flex flex-col sm:flex-row sm:items-center gap-3">
                <div class="flex-1">
                  <label class="block text-[11px] font-bold text-slate-700 mb-1">Enter 6-Digit Verification OTP *</label>
                  <input type="text" id="kycOtpInput" value="123456" maxlength="6" class="w-full text-xs font-mono tracking-widest bg-white border border-slate-300 rounded-xl p-2.5 text-slate-800 focus:outline-none focus:border-gov-teal" placeholder="123456">
                </div>
                <button type="button" onclick="confirmKycOtp()" class="mt-4 sm:mt-5 px-5 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white font-black rounded-xl text-xs shadow-sm flex items-center gap-1.5 shrink-0">
                  <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
                  <span>Verify Identity Token</span>
                </button>
              </div>
              <div class="text-[10px] text-slate-400">
                ⚡ Evaluator Hint: Pre-filled with demo OTP <strong>123456</strong> for instantaneous SIH testing.
              </div>
            </div>

            <!-- Verified Summary Card -->
            <div id="kycSuccessCard" class="hidden bg-emerald-50 border border-emerald-300 rounded-xl p-3.5 text-emerald-900 space-y-1">
              <div class="flex items-center gap-2 font-bold text-xs">
                <span class="w-4 h-4 rounded-full bg-emerald-600 text-white flex items-center justify-center text-[10px]">&check;</span>
                <span>KYC Identity Verification Complete</span>
              </div>
              <div class="text-[11px] text-emerald-800" id="kycSuccessDetails">
                Reference ID: DL-KYC-2026-98124 &bull; Provider: DigiLocker Sandbox &bull; Status: Verified
              </div>
            </div>

            <!-- Failed Summary Card -->
            <div id="kycFailedCard" class="hidden bg-rose-50 border border-rose-300 rounded-xl p-3 text-rose-900 flex items-center justify-between">
              <div class="flex items-center gap-2 text-xs font-semibold">
                <span>Verification failed or timed out. Please retry.</span>
              </div>
              <button type="button" onclick="initiateKycVerification()" class="px-3 py-1 bg-rose-600 text-white font-bold rounded-lg text-xs">Retry</button>
            </div>
          </div>
        </div>

        <!-- STEP 3: Complaint Details -->
        <div id="wizardStep3" class="hidden space-y-4">
          <div class="border-b border-slate-200 pb-2">
            <h4 class="text-sm font-extrabold text-gov-navy">Step 3: Target Institution &amp; Grievance Narrative</h4>
            <p class="text-xs text-slate-500">Provide details of the approved technical institute and the alleged violation.</p>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block font-bold text-slate-700 mb-1">Target Approved Institution *</label>
              <select id="wizInstSelect" required onchange="handleWizardInstChange(this.value)" class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-slate-800 focus:outline-none focus:border-gov-teal">
                <option value="1-3324567891">Apex Institute of Technology & Management (Pune)</option>
                <option value="1-4829103942">National Polytechnic & Science Academy (Ghaziabad)</option>
                <option value="1-5582910483">Imperial College of Engineering & Research (Bengaluru)</option>
                <option value="1-7729104851">Vanguard School of Business & Management (Noida)</option>
                <option value="1-9923847162">Saraswati College of Pharmacy & Health (Coimbatore)</option>
                <option value="OTHER">Other Approved Institution</option>
              </select>
            </div>
            <div>
              <label class="block font-bold text-slate-700 mb-1">AICTE Permanent ID *</label>
              <input type="text" id="wizAicteId" value="1-3324567891" readonly class="w-full text-xs font-mono bg-slate-100 border border-slate-300 rounded-xl p-2.5 text-slate-700 focus:outline-none">
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block font-bold text-slate-700 mb-1">Grievance Category *</label>
              <select id="wizCategory" required onchange="handleCategoryRoutingHint(this.value)" class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-slate-800 focus:outline-none focus:border-gov-teal">
                <option value="Faculty Qualifications & Pay Scale Violation">Faculty Qualifications &amp; 7th CPC Pay Scale Violation</option>
                <option value="Withholding of Original Certificates">Illegal Withholding of Original Certificates / Degrees</option>
                <option value="Capitation Fee & Excess Tuition Fee">Capitation Fee &amp; Excess Tuition Fee Demand</option>
                <option value="Unapproved Course Intake">Unapproved Student Intake / Extra Divisions</option>
                <option value="Denial of Refund on Admission Cancellation">Denial of Fee Refund on Admission Cancellation</option>
                <option value="Lack of Mandatory Laboratory Infrastructure">Lack of Mandatory Laboratory &amp; Computing Infrastructure</option>
                <option value="Student Harassment / Anti-Ragging Violation">Student Harassment / Anti-Ragging Non-Compliance</option>
              </select>
            </div>
            <div>
              <label class="block font-bold text-slate-700 mb-1">Intelligent Bureau Routing Indicator</label>
              <div id="wizRoutingHint" class="bg-blue-50 border border-blue-200 text-blue-900 rounded-xl p-2.5 text-xs font-semibold flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-blue-600"></span>
                <span>Regulation Bureau (RB) &bull; Statutory Norms Scrutiny</span>
              </div>
            </div>
          </div>

          <div>
            <label class="block font-bold text-slate-700 mb-1">Grievance Title / Subject *</label>
            <input type="text" id="wizTitle" required placeholder="Concise subject of the complaint..." class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-slate-800 focus:outline-none focus:border-gov-teal">
          </div>

          <div>
            <label class="block font-bold text-slate-700 mb-1">Detailed Grievance Narrative *</label>
            <textarea id="wizDescription" rows="4" required placeholder="Specify exact dates, affected students/faculty members, amounts demanded, and specific violations..." class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-slate-800 focus:outline-none focus:border-gov-teal"></textarea>
            <div class="text-[10px] text-slate-400 mt-1">
              * Text token Jaccard similarity will be calculated against existing complaints to flag cross-bureau overlap.
            </div>
          </div>
        </div>

        <!-- STEP 4: Upload Evidence -->
        <div id="wizardStep4" class="hidden space-y-4">
          <div class="border-b border-slate-200 pb-2">
            <h4 class="text-sm font-extrabold text-gov-navy">Step 4: Upload Supporting Evidence</h4>
            <p class="text-xs text-slate-500">Attach salary credit statements, fee receipts, photos of noticeboards, or signed affidavits.</p>
          </div>

          <div class="border-2 border-dashed border-slate-300 rounded-2xl p-6 text-center hover:border-gov-teal bg-slate-50 cursor-pointer" onclick="document.getElementById('wizFileInput').click()">
            <svg class="w-8 h-8 text-slate-400 mx-auto mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path></svg>
            <div class="text-xs font-bold text-slate-700">Click or Drag &amp; Drop Evidence Files Here</div>
            <div class="text-[11px] text-slate-400 mt-1">Supported: JPG, PNG, PDF up to 10MB per file</div>
            <input type="file" id="wizFileInput" class="hidden" multiple accept="image/jpeg,image/png,application/pdf" onchange="handleWizardFilesSelected(this)">
          </div>

          <!-- Uploaded Evidence List -->
          <div>
            <div class="text-xs font-bold text-slate-800 mb-2">Attached Evidence Items (<span id="wizFileCount">0</span>):</div>
            <div id="wizFileList" class="space-y-2">
              <div class="text-[11px] text-slate-400 italic bg-white p-3 rounded-xl border border-slate-200">
                No files uploaded yet. You can attach JPEG/PNG images or PDF documents.
              </div>
            </div>
          </div>
        </div>

        <!-- STEP 5: Evidence Screening (Hive AI) -->
        <div id="wizardStep5" class="hidden space-y-4">
          <div class="border-b border-slate-200 pb-2">
            <h4 class="text-sm font-extrabold text-gov-navy">Step 5: Hive AI Evidence Image Screening</h4>
            <p class="text-xs text-slate-500">Probabilistic synthetic image analysis via TheHive.ai (AI-generated image detection model).</p>
          </div>

          <div class="bg-slate-50 border border-slate-200 rounded-2xl p-4 space-y-3">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div>
                <div class="font-bold text-xs text-slate-900">Run Automated Evidence Screening</div>
                <div class="text-[11px] text-slate-500 mt-0.5">Scans uploaded image evidence for digital synthesis artifacts.</div>
              </div>
              <button type="button" id="btnRunHiveScreening" onclick="runHiveScreeningAction()" class="px-5 py-2.5 bg-purple-700 hover:bg-purple-600 text-white font-bold rounded-xl text-xs shadow-sm flex items-center gap-1.5 shrink-0">
                <svg class="w-4 h-4 text-purple-200" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path></svg>
                <span>Screen with Hive AI</span>
              </button>
            </div>

            <!-- Screening Progress Animation Bar -->
            <div id="hiveScreeningProgress" class="hidden space-y-2 pt-2">
              <div class="flex items-center justify-between text-[11px] font-bold text-purple-900">
                <span>Connecting to Hive AI Evidence Gateway...</span>
                <span id="hiveProgressPercent">45%</span>
              </div>
              <div class="w-full bg-slate-200 rounded-full h-2 overflow-hidden">
                <div id="hiveProgressBar" class="bg-gradient-to-r from-purple-600 to-indigo-500 h-2 rounded-full transition-all duration-300" style="width: 45%;"></div>
              </div>
            </div>

            <!-- Hive AI Screening Results Container -->
            <div id="hiveResultsContainer" class="space-y-2.5 pt-2">
              <!-- Dynamically populated -->
            </div>

            <!-- Important Limitations Callout -->
            <div class="bg-amber-50 border border-amber-300 rounded-xl p-3 text-amber-950 text-[11px] leading-relaxed flex items-start gap-2">
              <svg class="w-4 h-4 text-amber-600 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
              <div>
                <strong>Probabilistic Limitation Notice:</strong> AI detector outputs are indicators for human review, not absolute proof. A flagged image does not automatically invalidate a complaint or accuse the complainant. Human officer scrutiny is mandatory before any regulatory action.
              </div>
            </div>
          </div>
        </div>

        <!-- STEP 6: Review & Submit -->
        <div id="wizardStep6" class="hidden space-y-4">
          <div class="border-b border-slate-200 pb-2">
            <h4 class="text-sm font-extrabold text-gov-navy">Step 6: Review Summary &amp; Final Submission</h4>
            <p class="text-xs text-slate-500">Confirm all details before generating the official AICTE Case ID.</p>
          </div>

          <div class="bg-slate-50 border border-slate-200 rounded-2xl p-4 space-y-3">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs border-b border-slate-200 pb-3">
              <div>
                <span class="text-slate-400 font-bold uppercase text-[10px] block">Complainant Name &amp; KYC</span>
                <span class="font-extrabold text-slate-900" id="wizRevComplainant">--</span>
                <div class="text-[10px] text-emerald-600 font-bold" id="wizRevKycStatus">KYC: Verified</div>
              </div>
              <div>
                <span class="text-slate-400 font-bold uppercase text-[10px] block">Target Technical Institution</span>
                <span class="font-extrabold text-slate-900" id="wizRevInst">Apex Institute of Technology & Management</span>
                <div class="text-[10px] text-slate-500 font-mono" id="wizRevAicteId">AICTE ID: 1-3324567891</div>
              </div>
            </div>

            <div class="text-xs space-y-1 border-b border-slate-200 pb-3">
              <span class="text-slate-400 font-bold uppercase text-[10px] block">Category &amp; Assigned Bureau</span>
              <div class="font-bold text-slate-900" id="wizRevCategory">--</div>
              <div class="text-gov-blue font-bold" id="wizRevBureau">Regulation Bureau (RB)</div>
            </div>

            <div class="text-xs space-y-1 border-b border-slate-200 pb-3">
              <span class="text-slate-400 font-bold uppercase text-[10px] block">Subject Summary</span>
              <div class="font-bold text-slate-800" id="wizRevTitle">--</div>
            </div>

            <div class="text-xs space-y-1">
              <span class="text-slate-400 font-bold uppercase text-[10px] block">Evidence Screening Status</span>
              <div id="wizRevScreeningSummary" class="text-xs font-semibold text-slate-700">
                1 image screened (No AI Signal Detected) &bull; 1 document attached
              </div>
            </div>
          </div>

          <div class="flex items-start gap-2 pt-1 text-[11px] text-slate-600">
            <input type="checkbox" id="wizFinalConfirmCheck" required class="rounded border-slate-300 text-gov-teal focus:ring-gov-teal mt-0.5">
            <label for="wizFinalConfirmCheck">
              I solemnly confirm that the facts stated in this grievance are correct to the best of my knowledge and understand that false filings may attract proceedings under applicable laws.
            </label>
          </div>
        </div>

      </div>

      <!-- Wizard Bottom Navigation Bar -->
      <div class="bg-slate-100 px-6 py-3 border-t border-slate-200 flex items-center justify-between shrink-0">
        <button type="button" id="wizBtnPrev" onclick="prevWizardStep()" class="hidden px-4 py-2 border border-slate-300 rounded-xl text-slate-700 font-bold text-xs hover:bg-slate-200 transition-colors">
          &larr; Previous Step
        </button>
        <div></div>
        <div class="flex items-center gap-2">
          <button type="button" onclick="closeComplaintWizard()" class="px-4 py-2 text-slate-500 font-bold text-xs hover:text-slate-800">
            Cancel
          </button>
          <button type="button" id="wizBtnNext" onclick="nextWizardStep()" class="px-6 py-2.5 bg-gov-navy hover:bg-gov-darkNavy text-white font-bold rounded-xl text-xs transition-colors flex items-center gap-1.5 shadow-md">
            <span>Next: KYC Verification</span> &rarr;
          </button>
          <button type="button" id="wizBtnSubmit" onclick="submitWizardComplaint()" class="hidden px-6 py-2.5 bg-gradient-to-r from-gov-teal to-cyan-300 text-gov-darkNavy font-black rounded-xl text-xs transition-colors shadow-glow-teal flex items-center gap-1.5">
            <span>Submit Complaint &amp; Issue Case ID</span> &check;
          </button>
        </div>
      </div>

    </div>
  </div>

  <!-- ========================================== -->
  <!-- 3. LOGIN MODAL -->
  <!-- ========================================== -->
  <div id="loginModal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4 overflow-y-auto">
    <div class="max-w-4xl w-full bg-white rounded-3xl shadow-2xl border border-slate-700/50 overflow-hidden grid grid-cols-1 md:grid-cols-2 my-auto">
      
      <!-- Left Panel -->
      <div class="bg-gradient-to-br from-gov-navy to-gov-blue text-white p-8 flex flex-col justify-between relative overflow-hidden">
        <div class="absolute -right-10 -bottom-10 opacity-10 pointer-events-none">
          <svg class="w-72 h-72 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2L1 21h22L12 2zm0 3.99L19.53 19H4.47L12 5.99zM11 10h2v4h-2zm0 6h2v2h-2z"/></svg>
        </div>
        
        <div>
          <div class="flex items-center gap-2 mb-3">
            <span class="bg-gov-teal text-white text-[10px] font-black uppercase px-2 py-0.5 rounded tracking-wider">
              SIH 2026 EDITION
            </span>
            <span class="text-xs text-slate-300 font-mono">GOVERNMENT OF INDIA</span>
          </div>
          
          <div class="w-12 h-12 rounded-xl bg-gov-teal/20 border border-gov-teal text-cyan-200 flex items-center justify-center mb-4">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path>
            </svg>
          </div>

          <h2 class="text-xl font-black text-white tracking-tight leading-snug">
            Official Portal Sign In
          </h2>
          <p class="text-xs text-slate-300 mt-2 leading-relaxed">
            Enter your authorized email and password to access your role-based workspace.
          </p>
        </div>

        <div class="space-y-2 pt-6 border-t border-slate-700/60 text-xs text-slate-300">
          <div class="flex items-center gap-2">
            <svg class="w-4 h-4 text-cyan-300 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
            <span>Role-Based Access Governance (7 Roles)</span>
          </div>
          <div class="flex items-center gap-2">
            <svg class="w-4 h-4 text-cyan-300 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
            <span>SHA-256 Cryptographic Credential Hashing</span>
          </div>
        </div>

        <div class="text-[10px] text-slate-400 font-mono mt-6">
          Security Enclave: NIC / AICTE GovCloud Shield v4.8
        </div>
      </div>

      <!-- Right Form Panel -->
      <div class="p-8 flex flex-col justify-between text-slate-800">
        <div>
          <div class="flex items-center justify-between mb-2">
            <h3 class="text-lg font-black text-gov-navy tracking-tight">Portal Authentication</h3>
            <button onclick="closeLoginModal()" class="text-slate-400 hover:text-slate-700 text-xl font-bold">&times;</button>
          </div>
          <p class="text-xs text-slate-500 mb-3">
            Enter credentials below or select an instant evaluation role.
          </p>

          <!-- Quick Evaluator Fill Selector -->
          <div class="mb-3 bg-slate-50 p-2.5 rounded-xl border border-slate-200">
            <label class="block text-[9px] font-bold uppercase tracking-wider text-slate-500 mb-1.5">
              ⚡ Evaluator Quick Role Fill
            </label>
            <div class="grid grid-cols-2 gap-1 text-[11px]">
              <button type="button" onclick="selectDemoRole('rb_officer')" class="text-left p-1 rounded-lg border border-slate-200 hover:border-gov-teal hover:bg-white transition-all">
                <div class="font-bold text-blue-900 text-[10px]">1. Regulation Bureau</div>
              </button>
              <button type="button" onclick="selectDemoRole('pgrc_officer')" class="text-left p-1 rounded-lg border border-slate-200 hover:border-gov-teal hover:bg-white transition-all">
                <div class="font-bold text-purple-900 text-[10px]">2. PGRC Officer</div>
              </button>
              <button type="button" onclick="selectDemoRole('admin')" class="text-left p-1 rounded-lg border border-slate-200 hover:border-gov-teal hover:bg-white transition-all">
                <div class="font-bold text-slate-900 text-[10px]">3. Administrator</div>
              </button>
              <button type="button" onclick="selectDemoRole('college_inst')" class="text-left p-1 rounded-lg border border-slate-200 hover:border-gov-teal hover:bg-white transition-all">
                <div class="font-bold text-cyan-900 text-[10px]">4. College / Inst</div>
              </button>
            </div>
          </div>

          <!-- Error Alert Banner -->
          <div id="loginErrorAlert" class="hidden mb-3 bg-rose-50 border border-rose-300 text-rose-800 p-2.5 rounded-xl text-xs flex items-start gap-2">
            <svg class="w-4 h-4 text-rose-600 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            <span id="loginErrorText">Invalid credentials.</span>
          </div>

          <!-- Login Form -->
          <form onsubmit="handleLoginSubmit(event)" class="space-y-3">
            <div>
              <label class="block text-[11px] font-bold text-slate-700 uppercase mb-1">Official Email / Username *</label>
              <div class="relative">
                <input type="email" id="loginUsername" required value="arvind.joshi@aicte-india.org" placeholder="e.g. officer@aicte-india.org" class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl pl-9 pr-3 py-2 text-slate-800 focus:outline-none focus:border-gov-teal">
                <svg class="w-4 h-4 text-slate-400 absolute left-3 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207"></path></svg>
              </div>
            </div>

            <div>
              <label class="block text-[11px] font-bold text-slate-700 uppercase mb-1">Password *</label>
              <div class="relative">
                <input type="password" id="loginPassword" required value="AICTE@RB2026" class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl pl-9 pr-10 py-2 text-slate-800 focus:outline-none focus:border-gov-teal">
                <svg class="w-4 h-4 text-slate-400 absolute left-3 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
                <button type="button" onclick="togglePasswordVisibility()" class="absolute right-3 top-2 text-slate-400 hover:text-slate-600">
                  <svg id="eyeIcon" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                </button>
              </div>
            </div>

            <div class="flex items-center justify-between text-[11px]">
              <label class="flex items-center gap-1.5 cursor-pointer text-slate-600">
                <input type="checkbox" id="loginRememberMe" checked class="rounded border-slate-300 text-gov-teal focus:ring-gov-teal">
                <span>Remember session</span>
              </label>
              <a href="javascript:void(0)" onclick="showToast('Password recovery link dispatched to registered official mail.', 'info')" class="text-gov-lightBlue hover:underline font-semibold">Forgot Password?</a>
            </div>

            <button type="submit" class="w-full bg-gov-navy hover:bg-gov-darkNavy text-white font-bold py-2.5 rounded-xl shadow-md transition-all text-xs flex items-center justify-center gap-2 mt-2">
              <span>Authenticate &amp; Enter Portal</span>
              <svg class="w-4 h-4 text-cyan-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
            </button>
          </form>

          <!-- Links to Register and Landing Page -->
          <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-xs">
            <button type="button" onclick="switchToRegisterModal()" class="text-gov-lightBlue hover:underline font-semibold flex items-center gap-1">
              <span>New institution? Register here</span>
            </button>
            <button type="button" onclick="closeLoginModal(); showLandingPage();" class="text-slate-500 hover:text-slate-700">
              &larr; Return to Home
            </button>
          </div>

        </div>

        <div class="pt-3 border-t border-slate-100 text-[10px] text-slate-400 flex items-center justify-between mt-3">
          <span>AICTE Security Enclave</span>
          <span class="font-mono text-emerald-600 font-bold">256-Bit TLS</span>
        </div>
      </div>

    </div>
  </div>

  <!-- ========================================== -->
  <!-- 4. REGISTRATION MODAL (7 ROLES) -->
  <!-- ========================================== -->
  <div id="registerModal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4 overflow-y-auto">
    <div class="max-w-2xl w-full bg-white rounded-3xl shadow-2xl border border-slate-200 overflow-hidden my-auto flex flex-col max-h-[92vh]">
      
      <!-- Modal Header -->
      <div class="bg-gov-navy text-white px-6 py-4 flex items-center justify-between shrink-0">
        <div class="flex items-center gap-3">
          <div class="w-9 h-9 rounded-xl bg-gov-teal text-white flex items-center justify-center font-bold text-sm">
            +
          </div>
          <div>
            <h3 class="text-base font-extrabold tracking-tight">AICTE Portal Account Registration</h3>
            <p class="text-xs text-slate-300">Role-based institutional &amp; officer registration</p>
          </div>
        </div>
        <button onclick="closeRegisterModal()" class="text-slate-400 hover:text-white text-xl font-bold">&times;</button>
      </div>

      <!-- Registration Form Body -->
      <form id="registrationForm" onsubmit="handleRegisterSubmit(event)" class="p-6 overflow-y-auto flex-1 space-y-4 text-xs text-slate-700">
        
        <!-- Error Alert -->
        <div id="regErrorAlert" class="hidden bg-rose-50 border border-rose-300 text-rose-800 p-3 rounded-xl flex items-start gap-2">
          <svg class="w-4 h-4 text-rose-600 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          <span id="regErrorText">Please fill in all required fields.</span>
        </div>

        <!-- Role Selection (7 Roles) -->
        <div>
          <label class="block font-bold text-slate-700 uppercase mb-1">Select User Role *</label>
          <select id="regRole" required onchange="handleRoleFieldChange(this.value)" class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-slate-800 font-semibold focus:outline-none focus:border-gov-teal">
            <option value="college_inst">1. College / Institution (Technical College / Polytechnic)</option>
            <option value="university">2. University (Affiliating / Technical University)</option>
            <option value="rb_officer">3. Regulation Bureau (RB) Official</option>
            <option value="pgrc_officer">4. Public Grievance Redressal Cell (PGRC) Official</option>
            <option value="ro_officer">5. Regional Officer (RO - Western Region WRO)</option>
            <option value="senior_mgmt">6. Senior Management (Advisor / Member Secretary)</option>
            <option value="admin">7. System Administrator</option>
          </select>
        </div>

        <!-- Administrative Security Notice -->
        <div id="adminRoleSecurityNotice" class="hidden bg-amber-50 border border-amber-300 rounded-xl p-3 text-amber-900 text-[11px] leading-relaxed flex items-start gap-2">
          <svg class="w-4 h-4 text-amber-600 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
          <div>
            <strong>Administrative Privilege Governance Rule:</strong> Administrative and regulatory roles (Admin, Senior Management, RB, PGRC, Regional Officers) cannot self-assign privileged access. Your registration will remain marked as <em>Pending Administrator Verification</em> until manually approved by an authorized AICTE Administrator.
          </div>
        </div>

        <!-- Dynamic Role-Specific Fields Container -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div id="regOrgContainer">
            <label class="block font-bold text-slate-700 mb-1" id="regOrgLabel">Organization / Institution Name *</label>
            <input type="text" id="regOrgName" required placeholder="e.g. Apex Institute of Technology & Management" class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-slate-800 focus:outline-none focus:border-gov-teal">
          </div>

          <div id="regAicteIdContainer">
            <label class="block font-bold text-slate-700 mb-1" id="regAicteIdLabel">AICTE Permanent ID *</label>
            <input type="text" id="regAicteId" placeholder="e.g. 1-3324567891" class="w-full text-xs font-mono bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-slate-800 focus:outline-none focus:border-gov-teal">
          </div>
        </div>

        <!-- Common Personal / Official Details -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label class="block font-bold text-slate-700 mb-1">Full Name *</label>
            <input type="text" id="regName" required placeholder="Authorized representative / officer name" class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-slate-800 focus:outline-none focus:border-gov-teal">
          </div>

          <div>
            <label class="block font-bold text-slate-700 mb-1">Official Email Address *</label>
            <input type="email" id="regEmail" required placeholder="e.g. principal@institution.edu.in" class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-slate-800 focus:outline-none focus:border-gov-teal">
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label class="block font-bold text-slate-700 mb-1">Contact Mobile Number *</label>
            <input type="tel" id="regPhone" required placeholder="+91 98765 43210" class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-slate-800 focus:outline-none focus:border-gov-teal">
          </div>

          <div>
            <label class="block font-bold text-slate-700 mb-1">State / AICTE Region</label>
            <select id="regRegion" class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-slate-800 focus:outline-none focus:border-gov-teal">
              <option value="Western Region (WRO - Mumbai)">Western Region (WRO - Maharashtra, Goa)</option>
              <option value="Northern Region (NRO - Kanpur)">Northern Region (NRO - UP, Uttarakhand)</option>
              <option value="Southern Region (SRO - Chennai)">Southern Region (SRO - Tamil Nadu)</option>
              <option value="South-Western Region (SWRO - Bengaluru)">South-Western Region (SWRO - Karnataka, Kerala)</option>
              <option value="North-West Region (NWRO - Chandigarh)">North-West Region (NWRO - Delhi, Punjab, Haryana)</option>
            </select>
          </div>
        </div>

        <!-- Password and Confirm Password -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label class="block font-bold text-slate-700 mb-1">Create Password * (min 8 chars)</label>
            <input type="password" id="regPassword" required minlength="8" placeholder="••••••••" class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-slate-800 focus:outline-none focus:border-gov-teal">
          </div>

          <div>
            <label class="block font-bold text-slate-700 mb-1">Confirm Password *</label>
            <input type="password" id="regConfirmPassword" required minlength="8" placeholder="••••••••" class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-slate-800 focus:outline-none focus:border-gov-teal">
          </div>
        </div>

        <div class="flex items-start gap-2 pt-1 text-[11px] text-slate-600">
          <input type="checkbox" id="regConsent" required class="rounded border-slate-300 text-gov-teal focus:ring-gov-teal mt-0.5">
          <label for="regConsent">
            I certify that the information provided represents an authorized institutional representative or regulatory personnel under AICTE Act guidelines.
          </label>
        </div>

        <div class="pt-3 border-t border-slate-200 flex flex-wrap items-center justify-between gap-3">
          <button type="button" onclick="switchToLoginModal()" class="text-xs text-gov-lightBlue hover:underline font-semibold">
            Already have an account? Sign in
          </button>
          
          <div class="flex items-center gap-2">
            <button type="button" onclick="closeRegisterModal()" class="px-4 py-2 rounded-xl border border-slate-300 text-slate-600 font-bold hover:bg-slate-100 transition-colors">
              Cancel
            </button>
            <button type="submit" class="bg-gov-teal hover:bg-gov-darkTeal text-white font-bold px-6 py-2 rounded-xl shadow-md transition-all">
              Complete Registration
            </button>
          </div>
        </div>

      </form>

    </div>
  </div>

  <!-- ========================================== -->
  <!-- 5. CASE DETAIL MODAL & AUDIT TIMELINE -->
  <!-- ========================================== -->
  <div id="complaintDetailModal" class="hidden fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-4 overflow-y-auto">
    <div class="bg-white rounded-2xl shadow-modal border border-slate-200 max-w-4xl w-full max-h-[90vh] flex flex-col overflow-hidden my-auto">
      
      <!-- Modal Header -->
      <div class="bg-gov-navy text-white px-6 py-4 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 rounded-lg bg-gov-teal text-white flex items-center justify-center font-bold text-xs">
            DOC
          </div>
          <div>
            <div class="flex items-center gap-2">
              <h3 class="text-base font-extrabold tracking-tight" id="modalCaseId">AICTE/RB/2026/0104</h3>
              <span id="modalCaseStatusBadge" class="badge bg-blue-100 text-blue-900">Under Process</span>
              <span id="modalCasePriorityBadge" class="badge bg-rose-100 text-rose-900">Urgent</span>
            </div>
            <p class="text-xs text-slate-300" id="modalInstName">Apex Institute of Technology & Management</p>
          </div>
        </div>
        <button onclick="closeComplaintDetailModal()" class="text-slate-400 hover:text-white text-xl font-bold">&times;</button>
      </div>

      <!-- Modal Body -->
      <div class="p-6 overflow-y-auto flex-1 space-y-6 text-xs text-slate-700">
        
        <!-- Overlap Alert Badge inside Case Details if linked/potential -->
        <div id="modalOverlapNotice" class="hidden bg-amber-50 border border-amber-300 rounded-xl p-3.5 flex items-start gap-3">
          <svg class="w-5 h-5 text-amber-600 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
          <div>
            <div class="font-bold text-amber-900">Cross-Bureau Link Established</div>
            <p class="text-amber-800 text-[11px] mt-0.5" id="modalOverlapNoticeText">
              This case is linked to concurrent case <strong>AICTE/PGRC/2026/0218</strong> handled by PGRC. Shared remarks are recorded below.
            </p>
          </div>
        </div>

        <!-- Core Details Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 bg-slate-50 p-4 rounded-xl border border-slate-200">
          <div>
            <div class="text-[10px] uppercase font-bold text-slate-400">AICTE Permanent ID</div>
            <div class="font-bold text-slate-900 text-sm font-mono mt-0.5" id="modalAicteId">1-3324567891</div>
          </div>
          <div>
            <div class="text-[10px] uppercase font-bold text-slate-400">Assigned Bureau &amp; Officer</div>
            <div class="font-bold text-gov-blue text-sm mt-0.5" id="modalBureauOfficer">Regulation Bureau</div>
          </div>
          <div>
            <div class="text-[10px] uppercase font-bold text-slate-400">Date Received &amp; Complainant</div>
            <div class="font-bold text-slate-800 text-sm mt-0.5" id="modalDateReceived">12 Mar 2026</div>
          </div>
        </div>

        <!-- Grievance Description -->
        <div>
          <h4 class="font-bold text-slate-900 uppercase tracking-wider text-[11px] mb-1.5">Official Grievance Narrative</h4>
          <div class="p-3.5 bg-white border border-slate-200 rounded-xl leading-relaxed text-slate-800" id="modalDescription">
            --
          </div>
        </div>

        <!-- KYC Verification Record -->
        <div id="modalKycSection" class="p-3.5 bg-slate-50 border border-slate-200 rounded-xl">
          <div class="flex items-center justify-between mb-1">
            <span class="font-bold text-slate-900 uppercase tracking-wider text-[11px]">Complainant KYC Verification Record</span>
            <span id="modalKycBadge" class="badge bg-emerald-100 text-emerald-800">Verified</span>
          </div>
          <div class="text-xs text-slate-600 space-y-0.5" id="modalKycDetails">
            <div>Provider: DigiLocker Sandbox &bull; Ref: DL-KYC-2026-98124</div>
            <div class="text-[11px] text-slate-500">Identity verified against verified institutional roster.</div>
          </div>
        </div>

        <!-- Evidence & Documents with Hive AI Status -->
        <div>
          <h4 class="font-bold text-slate-900 uppercase tracking-wider text-[11px] mb-2">Attached Evidence &amp; Hive AI Screening Dossier</h4>
          <div id="modalDocsContainer" class="space-y-2">
            <!-- Dynamically populated -->
          </div>
        </div>

        <!-- Officer Evidence Review Action Form (Section 8: RB & PGRC) -->
        <div id="modalOfficerReviewSection" class="bg-blue-50/50 border border-blue-200 rounded-xl p-4 space-y-3">
          <div class="flex items-center justify-between">
            <h4 class="font-bold text-gov-navy uppercase tracking-wider text-[11px]">Officer Evidence Scrutiny Decision</h4>
            <span class="text-[10px] text-slate-500 font-mono">Restricted to Assigned Bureau</span>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div>
              <label class="block text-[10px] font-bold text-slate-700 uppercase mb-1">Review Decision *</label>
              <select id="modalOfficerDecisionSelect" class="w-full text-xs bg-white border border-slate-300 rounded-lg p-2 text-slate-800 font-bold focus:outline-none focus:border-gov-teal">
                <option value="Accept for Further Review">Accept for Further Review</option>
                <option value="Request Additional Evidence">Request Additional Evidence</option>
                <option value="Escalate for Investigation">Escalate for Investigation</option>
              </select>
            </div>
            <div class="sm:col-span-2">
              <label class="block text-[10px] font-bold text-slate-700 uppercase mb-1">Officer Reasoning &amp; Internal Notes *</label>
              <input type="text" id="modalOfficerReasoningInput" placeholder="Specify observations, regulatory clauses, or directives..." class="w-full text-xs bg-white border border-slate-300 rounded-lg p-2 text-slate-800 focus:outline-none focus:border-gov-teal">
            </div>
          </div>

          <div class="flex justify-end">
            <button type="button" onclick="submitOfficerEvidenceDecisionModal()" class="px-4 py-2 bg-gov-navy hover:bg-gov-darkNavy text-white font-bold rounded-lg text-xs flex items-center gap-1.5 shadow-sm">
              <svg class="w-4 h-4 text-cyan-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
              <span>Record Officer Decision</span>
            </button>
          </div>
        </div>

        <!-- Chronological Timeline -->
        <div>
          <h4 class="font-bold text-slate-900 uppercase tracking-wider text-[11px] mb-3">Chronological Workflow &amp; Audit Trail</h4>
          <div id="modalTimeline" class="space-y-3 relative before:absolute before:inset-0 before:left-3.5 before:w-0.5 before:bg-slate-200">
            <!-- Dynamically populated -->
          </div>
        </div>

      </div>

      <!-- Modal Footer -->
      <div class="bg-slate-100 px-6 py-3 border-t border-slate-200 flex justify-end">
        <button onclick="closeComplaintDetailModal()" class="bg-slate-200 hover:bg-slate-300 text-slate-700 font-bold px-4 py-1.5 rounded-lg text-xs">
          Close Dossier
        </button>
      </div>

    </div>
  </div>

  <!-- ========================================== -->
  <!-- 6. PUBLIC TRACKING MODAL -->
  <!-- ========================================== -->
  <div id="trackComplaintModal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4 overflow-y-auto">
    <div class="max-w-2xl w-full bg-white rounded-3xl shadow-2xl border border-slate-200 overflow-hidden my-auto flex flex-col">
      <div class="bg-gov-navy text-white px-6 py-4 flex items-center justify-between">
        <div>
          <span class="text-[10px] font-bold text-cyan-300 uppercase tracking-wider">Live Status Lookup</span>
          <h3 class="text-base font-extrabold tracking-tight" id="trackModalCaseId">AICTE/RB/2026/0104</h3>
        </div>
        <button onclick="closeTrackModal()" class="text-slate-400 hover:text-white text-xl font-bold">&times;</button>
      </div>
      
      <div class="p-6 space-y-4 text-xs text-slate-700" id="trackModalBody">
        <!-- Dynamically rendered -->
      </div>
      
      <div class="bg-slate-50 px-6 py-3 border-t border-slate-100 flex items-center justify-between">
        <span class="text-[10px] text-slate-500 font-mono">Status verified by AICTE Central National Grievance Grid</span>
        <button onclick="closeTrackModal()" class="px-4 py-1.5 bg-gov-navy text-white font-bold rounded-lg text-xs">Close</button>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- 7. INTER-BUREAU COORDINATION MODAL -->
  <!-- ========================================== -->
  <div id="coordinationModal" class="hidden fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-4 overflow-y-auto">
    <div class="bg-white rounded-2xl shadow-modal border border-slate-200 max-w-xl w-full p-6 text-xs text-slate-700 space-y-4">
      <div class="flex items-center justify-between border-b border-slate-200 pb-3">
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-amber-500 animate-pulse"></span>
          <h3 class="text-base font-extrabold text-gov-navy">Establish Inter-Bureau Coordination Link</h3>
        </div>
        <button onclick="closeCoordinationModal()" class="text-slate-400 hover:text-slate-600 text-lg font-bold">&times;</button>
      </div>

      <p class="text-slate-600 leading-relaxed">
        You are linking <strong>Case A (Regulation Bureau)</strong> with <strong>Case B (PGRC)</strong>. This synchronizes inquiry notes, alerts assigned officers from both bureaus, and schedules a coordinated inspection.
      </p>

      <div>
        <label class="block font-bold text-slate-700 uppercase text-[10px] mb-1">Joint Coordination Remarks / Directive *</label>
        <textarea id="coordinationRemarks" rows="3" class="w-full text-xs bg-slate-50 border border-slate-300 rounded-lg p-2.5 text-slate-800 focus:outline-none focus:border-gov-teal" placeholder="e.g. Conduct joint scrutiny with Western Regional Office on 28 Oct 2026. Consolidated compliance affidavit to be submitted by Chairman."></textarea>
      </div>

      <div class="bg-amber-50 border border-amber-200 p-3 rounded-xl text-[11px] text-amber-900 flex items-start gap-2">
        <svg class="w-4 h-4 text-amber-600 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
        <span>
          <strong>Human-in-the-loop governance:</strong> Linking creates cross-reference pointers and joint notices. Neither complaint is auto-closed without formal officer disposal orders.
        </span>
      </div>

      <div class="flex items-center justify-end gap-2 pt-2">
        <button onclick="closeCoordinationModal()" class="px-4 py-2 rounded-lg border border-slate-300 text-slate-600 font-bold hover:bg-slate-100">
          Cancel
        </button>
        <button onclick="confirmLinkCases()" class="bg-gov-teal hover:bg-gov-darkTeal text-white font-bold px-5 py-2 rounded-lg shadow-sm">
          Confirm Joint Linking &amp; Notify Officers
        </button>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- 8. ABOUT SYSTEM MODAL -->
  <!-- ========================================== -->
  <div id="aboutModal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4 overflow-y-auto">
    <div class="max-w-2xl w-full bg-white rounded-3xl shadow-2xl border border-slate-200 overflow-hidden my-auto flex flex-col max-h-[90vh]">
      <div class="bg-gov-navy text-white px-6 py-4 flex items-center justify-between">
        <h3 class="text-base font-extrabold tracking-tight">About AICTE Institution Complaint Monitoring System</h3>
        <button onclick="closeAboutModal()" class="text-slate-400 hover:text-white text-xl font-bold">&times;</button>
      </div>
      <div class="p-6 overflow-y-auto space-y-4 text-xs text-slate-700 leading-relaxed">
        <p>
          The <strong>AICTE Integrated Institution Complaint Monitoring &amp; Tracking Dashboard</strong> was developed for the <strong>Smart India Hackathon (SIH 2026)</strong>.
        </p>
        <p>
          Historically, technical education grievances were fragmented across multiple independent bureaus: the <em>Regulation Bureau (RB)</em> for institutional compliance, the <em>Public Grievance Redressal Cell (PGRC)</em> for student and faculty grievances, and the <em>Regional Offices (ROs)</em> for ground inspections.
        </p>
        <div class="bg-blue-50 border border-blue-200 rounded-xl p-4 space-y-2">
          <div class="font-bold text-gov-navy text-sm">Key Architectural Breakthroughs:</div>
          <ul class="list-disc pl-5 space-y-1 text-slate-700">
            <li><strong>AI-Assisted Cross-Bureau Overlap Detection:</strong> Multi-factor similarity algorithms scan AICTE Permanent IDs, concurrent bureau jurisdictions, correlated violation categories, and grievance token Jaccard text similarity.</li>
            <li><strong>7-Role Enterprise Governance:</strong> Strict permission boundaries for RB, PGRC, Administrators, Western Regional Office (WRO), Senior Management (Council Secretariat), Colleges, and Affiliating Universities.</li>
            <li><strong>Hive AI Synthetic Image Screening:</strong> Automated evidence analysis flags digital manipulation in uploaded photographic evidence while mandating human officer review.</li>
            <li><strong>Mandatory KYC Verification:</strong> Pre-submission identity verification ensures accountable, non-frivolous complaints.</li>
          </ul>
        </div>
      </div>
      <div class="bg-slate-50 px-6 py-3 border-t border-slate-100 flex justify-end">
        <button onclick="closeAboutModal()" class="px-4 py-2 bg-gov-navy text-white font-bold rounded-xl text-xs">Close</button>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- 9. HELP & SUPPORT MODAL -->
  <!-- ========================================== -->
  <div id="helpModal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4 overflow-y-auto">
    <div class="max-w-2xl w-full bg-white rounded-3xl shadow-2xl border border-slate-200 overflow-hidden my-auto flex flex-col max-h-[90vh]">
      <div class="bg-gov-navy text-white px-6 py-4 flex items-center justify-between">
        <h3 class="text-base font-extrabold tracking-tight">AICTE Helpdesk &amp; Support Channels</h3>
        <button onclick="closeHelpModal()" class="text-slate-400 hover:text-white text-xl font-bold">&times;</button>
      </div>
      <div class="p-6 overflow-y-auto space-y-4 text-xs text-slate-700">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200">
            <div class="font-bold text-slate-900 text-sm">Central Redressal Helpline</div>
            <div class="text-xs text-gov-lightBlue font-bold mt-1">Toll-Free: 1800-11-2323</div>
            <div class="text-[11px] text-slate-500 mt-1">Monday &ndash; Friday (09:30 AM &ndash; 05:30 PM IST)</div>
          </div>
          <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200">
            <div class="font-bold text-slate-900 text-sm">Official Grievance Email</div>
            <div class="text-xs text-gov-lightBlue font-bold mt-1">grievance-support@aicte-india.org</div>
            <div class="text-[11px] text-slate-500 mt-1">Technical desk for portal issues &amp; KYC errors.</div>
          </div>
        </div>

        <div>
          <h4 class="font-bold text-slate-900 mb-2">Frequently Asked Questions</h4>
          <div class="space-y-2">
            <div class="p-3 bg-white border border-slate-200 rounded-xl">
              <div class="font-bold text-slate-800">Q: Why is KYC verification mandatory before filing?</div>
              <div class="text-[11px] text-slate-600 mt-1">A: Section 5 mandates verification to deter fraudulent or malicious petitions while protecting genuine faculty and student complainants.</div>
            </div>
            <div class="p-3 bg-white border border-slate-200 rounded-xl">
              <div class="font-bold text-slate-800">Q: What happens if Hive AI flags my uploaded image?</div>
              <div class="text-[11px] text-slate-600 mt-1">A: AI image detection is probabilistic and does NOT automatically reject your grievance. It alerts the assigned officer to conduct forensic scrutiny.</div>
            </div>
          </div>
        </div>
      </div>
      <div class="bg-slate-50 px-6 py-3 border-t border-slate-100 flex justify-end">
        <button onclick="closeHelpModal()" class="px-4 py-2 bg-gov-navy text-white font-bold rounded-xl text-xs">Close</button>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- 10. AICTE GUIDELINES / RESOLUTION MODAL -->
  <!-- ========================================== -->
  <div id="guidelinesModal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4 overflow-y-auto">
    <div class="max-w-2xl w-full bg-white rounded-3xl shadow-2xl border border-slate-200 overflow-hidden my-auto flex flex-col max-h-[90vh]">
      <div class="bg-gov-navy text-white px-6 py-4 flex items-center justify-between">
        <h3 class="text-base font-extrabold tracking-tight">AICTE Grievance Redressal Regulations</h3>
        <button onclick="closeGuidelinesModal()" class="text-slate-400 hover:text-white text-xl font-bold">&times;</button>
      </div>
      <div class="p-6 overflow-y-auto space-y-4 text-xs text-slate-700 leading-relaxed">
        <div class="p-3.5 bg-amber-50 border border-amber-200 rounded-xl text-amber-950">
          <strong>Official Gazette Notification Reference:</strong> F. No. 1-101/PGRC/AICTE/Regulation/2019 under the All India Council for Technical Education (Redressal of Grievance of Faculty/Students) Regulations.
        </div>
        <div>
          <h4 class="font-bold text-slate-900 text-sm mb-1">Key Statutory Mandates</h4>
          <ul class="list-disc pl-5 space-y-1.5 text-slate-700">
            <li><strong>Mandatory Appointment of Ombudsman:</strong> Every affiliating university and technical institution must appoint an independent Ombudsman for student disputes.</li>
            <li><strong>Prohibition of Certificate Retention:</strong> Institutions are strictly prohibited from retaining original educational certificates of admitted students or appointed faculty.</li>
            <li><strong>7th CPC Minimum Pay Scales:</strong> Approved technical institutions must disburse salaries via direct bank transfers compliant with AICTE 7th CPC entry pay scales.</li>
            <li><strong>Full Fee Refund:</strong> On withdrawal before the cutoff date, institutions must refund tuition fees with a maximum deduction of Rs. 1,000 as processing charges.</li>
          </ul>
        </div>
      </div>
      <div class="bg-slate-50 px-6 py-3 border-t border-slate-100 flex justify-end">
        <button onclick="closeGuidelinesModal()" class="px-4 py-2 bg-gov-navy text-white font-bold rounded-xl text-xs">Close</button>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- 11. INSTITUTIONS DIRECTORY MODAL -->
  <!-- ========================================== -->
  <div id="institutionsDirectoryModal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4 overflow-y-auto">
    <div class="max-w-4xl w-full bg-white rounded-3xl shadow-2xl border border-slate-200 overflow-hidden my-auto flex flex-col max-h-[90vh]">
      <div class="bg-gov-navy text-white px-6 py-4 flex items-center justify-between">
        <div>
          <h3 class="text-base font-extrabold tracking-tight">Approved Technical Institutions Directory</h3>
          <p class="text-xs text-slate-300">Search permanent IDs, regional office jurisdictions, and regulatory dossiers</p>
        </div>
        <button onclick="closeInstitutionsDirectoryModal()" class="text-slate-400 hover:text-white text-xl font-bold">&times;</button>
      </div>
      <div class="p-6 overflow-y-auto space-y-4 text-xs text-slate-700">
        <div class="border border-slate-200 rounded-2xl overflow-hidden">
          <table class="w-full text-left">
            <thead class="bg-slate-100 text-slate-700 font-bold uppercase text-[10px]">
              <tr>
                <th class="py-3 px-3">Permanent ID</th>
                <th class="py-3 px-3">Institution Name</th>
                <th class="py-3 px-3">Region</th>
                <th class="py-3 px-3">Approval Status</th>
                <th class="py-3 px-3 text-right">Dossier</th>
              </tr>
            </thead>
            <tbody id="directoryTableBody" class="divide-y divide-slate-100">
              <!-- Dynamically populated -->
            </tbody>
          </table>
        </div>
      </div>
      <div class="bg-slate-50 px-6 py-3 border-t border-slate-100 flex justify-end">
        <button onclick="closeInstitutionsDirectoryModal()" class="px-4 py-2 bg-gov-navy text-white font-bold rounded-xl text-xs">Close</button>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- 12. INSTITUTION PROFILE DOSSIER MODAL -->
  <!-- ========================================== -->
  <div id="institutionModal" class="hidden fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-4 overflow-y-auto">
    <div class="bg-white rounded-2xl shadow-modal border border-slate-200 max-w-3xl w-full max-h-[90vh] flex flex-col overflow-hidden my-auto">
      <div class="bg-gov-navy text-white px-6 py-4 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 rounded-lg bg-gov-lightBlue text-white flex items-center justify-center font-bold text-xs">
            INST
          </div>
          <div>
            <h3 class="text-base font-extrabold tracking-tight" id="instModalName">Institution Profile</h3>
            <p class="text-xs text-slate-300" id="instModalSub">Comprehensive Complaint &amp; Regulatory Dossier</p>
          </div>
        </div>
        <button onclick="closeInstitutionModal()" class="text-slate-400 hover:text-white text-xl font-bold">&times;</button>
      </div>

      <div class="p-6 overflow-y-auto flex-1 space-y-6 text-xs text-slate-700">
        <!-- Info Cards -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 bg-slate-50 p-4 rounded-xl border border-slate-200">
          <div>
            <div class="text-[10px] uppercase font-bold text-slate-400">AICTE Permanent ID</div>
            <div class="font-bold text-slate-900 text-sm font-mono mt-0.5" id="instModalId">--</div>
          </div>
          <div>
            <div class="text-[10px] uppercase font-bold text-slate-400">State / Region</div>
            <div class="font-bold text-slate-800 text-sm mt-0.5" id="instModalRegion">--</div>
          </div>
          <div>
            <div class="text-[10px] uppercase font-bold text-slate-400">Approval Status</div>
            <div class="font-bold text-emerald-600 text-sm mt-0.5" id="instModalStatus">Approved (EOA 2025-26)</div>
          </div>
          <div>
            <div class="text-[10px] uppercase font-bold text-slate-400">Head of Institution</div>
            <div class="font-bold text-slate-800 text-sm mt-0.5" id="instModalHead">--</div>
          </div>
        </div>

        <!-- Active Regulatory Actions -->
        <div>
          <h4 class="font-bold text-slate-900 uppercase tracking-wider text-[11px] mb-2">Active Regulatory Sanctions &amp; Directives</h4>
          <div id="instModalActionsList" class="space-y-1.5">
            <!-- Injected -->
          </div>
        </div>

        <!-- Linked Complaints Table for this Institution -->
        <div>
          <h4 class="font-bold text-slate-900 uppercase tracking-wider text-[11px] mb-2">Complete Inter-Bureau Complaint History</h4>
          <div class="border border-slate-200 rounded-xl overflow-hidden">
            <table class="w-full text-left text-xs text-slate-600">
              <thead class="bg-slate-100 text-slate-700 font-bold uppercase text-[10px]">
                <tr>
                  <th class="py-2.5 px-3">Case ID</th>
                  <th class="py-2.5 px-3">Bureau</th>
                  <th class="py-2.5 px-3">Category</th>
                  <th class="py-2.5 px-3">Status</th>
                  <th class="py-2.5 px-3 text-right">Action</th>
                </tr>
              </thead>
              <tbody id="instModalComplaintsTable" class="divide-y divide-slate-100">
                <!-- Injected -->
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <div class="bg-slate-100 px-6 py-3 border-t border-slate-200 flex justify-end">
        <button onclick="closeInstitutionModal()" class="bg-slate-200 hover:bg-slate-300 text-slate-700 font-bold px-4 py-1.5 rounded-lg text-xs">
          Close Profile
        </button>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- 13. REGISTRATION SUCCESS CONFIRMATION MODAL -->
  <!-- ========================================== -->
  <div id="regSuccessModal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4">
    <div class="max-w-md w-full bg-white rounded-3xl shadow-2xl border border-slate-200 p-6 text-center space-y-4 my-auto">
      <div class="w-14 h-14 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center mx-auto text-2xl font-black">
        &check;
      </div>
      <h3 class="text-lg font-black text-gov-navy" id="regSuccessTitle">Registration Successful</h3>
      <p class="text-xs text-slate-600 leading-relaxed" id="regSuccessMessage">
        Your account has been registered in the AICTE Institution Complaint Monitoring System.
      </p>
      <div class="pt-2 flex flex-col sm:flex-row gap-2 justify-center">
        <button onclick="closeRegSuccessModal(); showLoginModal();" class="px-5 py-2.5 bg-gov-navy hover:bg-gov-darkNavy text-white font-bold rounded-xl text-xs transition-colors">
          Proceed to Sign In
        </button>
        <button onclick="closeRegSuccessModal(); showLandingPage();" class="px-4 py-2.5 border border-slate-300 text-slate-700 font-bold rounded-xl text-xs hover:bg-slate-50">
          Return to Home
        </button>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- 14. COMPLAINT CONFIRMATION MODAL -->
  <!-- ========================================== -->
  <div id="complaintConfirmationModal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4">
    <div class="max-w-lg w-full bg-white rounded-3xl shadow-2xl border border-slate-200 p-6 text-center space-y-4 my-auto">
      <div class="w-14 h-14 rounded-full bg-gov-teal/20 text-gov-teal flex items-center justify-center mx-auto text-2xl font-black">
        &check;
      </div>
      <span class="text-[10px] font-black uppercase tracking-wider text-gov-teal bg-gov-teal/10 px-2 py-0.5 rounded">
        Complaint Registered Successfully
      </span>
      <h3 class="text-lg font-black text-gov-navy">AICTE Case Reference Issued</h3>
      
      <div class="bg-slate-50 border border-slate-200 rounded-2xl p-4 text-left space-y-2">
        <div class="flex items-center justify-between border-b border-slate-200 pb-2">
          <span class="text-xs text-slate-500">Official Case ID:</span>
          <span class="text-sm font-black font-mono text-gov-lightBlue" id="confCaseId">AICTE/RB/2026/0126</span>
        </div>
        <div class="flex items-center justify-between text-xs">
          <span class="text-slate-500">Target Institution:</span>
          <span class="font-bold text-slate-800" id="confInstName">--</span>
        </div>
        <div class="flex items-center justify-between text-xs">
          <span class="text-slate-500">Assigned Bureau:</span>
          <span class="font-bold text-blue-900" id="confBureau">Regulation Bureau</span>
        </div>
        <div class="flex items-center justify-between text-xs">
          <span class="text-slate-500">Resolution SLA Forecast:</span>
          <span class="font-bold text-emerald-600" id="confSla">30 Days (Due: 28 Nov 2026)</span>
        </div>
      </div>

      <p class="text-xs text-slate-500 leading-relaxed">
        Save this Case ID for status inquiries. You can track this case anytime using the Public Tracking Desk on the home page.
      </p>

      <div class="pt-2 flex flex-col sm:flex-row gap-2 justify-center">
        <button onclick="closeComplaintConfModal(); trackComplaintPublic(lastSubmittedCaseId);" class="px-5 py-2.5 bg-gov-navy hover:bg-gov-darkNavy text-white font-bold rounded-xl text-xs transition-colors">
          Track This Case Now
        </button>
        <button onclick="closeComplaintConfModal(); showLandingPage();" class="px-4 py-2.5 border border-slate-300 text-slate-700 font-bold rounded-xl text-xs hover:bg-slate-50">
          Back to Home
        </button>
      </div>
    </div>
  </div>

  <!-- TOAST NOTIFICATION CONTAINER -->
  <div id="toastContainer" class="fixed bottom-5 right-5 z-50 flex flex-col gap-2 pointer-events-none"></div>
'''
