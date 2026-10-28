# -*- coding: utf-8 -*-
"""
Portal views and workspaces for AICTE Complaint Monitoring System.
Defines:
- Top Portal Header & Navigation Bar
- Shared tab containers (Dashboard, Complaints, Overlap, Institutions, Reports, Users)
- 7 Dedicated Role Portals:
  1. Regulation Bureau (RB) Portal with Dedicated Evidence Review Workspace
  2. Public Grievance Redressal Cell (PGRC) Portal with Dedicated Evidence Review Workspace
  3. Admin Portal with User Management, Approvals & Audit Trail
  4. Regional Officer (WRO) Portal with strict regional data boundaries
  5. Senior Management Portal with Council KPIs & Executive Report Export
  6. College / Institution Portal with private institutional complaints & compliance submission
  7. University Portal with Affiliated Institutions Compliance Matrix
"""

def get_portal_html():
    return '''  <!-- ========================================== -->
  <!-- 3. PORTAL CONTAINER & WORKSPACE (AUTHENTICATED) -->
  <!-- ========================================== -->
  <div id="portalContainer" class="hidden min-h-screen flex flex-col bg-slate-50">
    
    <!-- Top Government Header Banner -->
    <header id="portalHeader" class="bg-gov-darkNavy text-white border-b border-slate-800 text-xs px-4 py-2 flex flex-wrap justify-between items-center z-40">
      <div class="flex items-center gap-3">
        <span class="inline-flex items-center gap-1.5 font-semibold text-slate-300">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
          AICTE Official Grievance &amp; Compliance Enclave
        </span>
        <span class="hidden md:inline text-slate-500">|</span>
        <span class="hidden md:inline text-slate-400">Ministry of Education, Government of India</span>
      </div>
      <div class="flex items-center gap-4 text-slate-400">
        <div id="portalLiveClock" class="font-mono text-slate-300 text-xs hidden sm:block">--:--:-- IST</div>
        <button onclick="showLandingPage()" class="text-cyan-300 hover:text-white transition-colors flex items-center gap-1 text-xs font-bold">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>
          <span>Return to Home</span>
        </button>
      </div>
    </header>

    <!-- Portal Navigation Bar with Role Selector & Profile -->
    <nav id="portalNav" class="bg-gov-navy text-white sticky top-0 z-40 shadow-lg border-b border-blue-900/60">
      <div class="max-w-7xl mx-auto px-4 sm:px-6">
        <div class="flex items-center justify-between h-16">
          
          <!-- Logo & Brand -->
          <div class="flex items-center gap-3 cursor-pointer" onclick="showLandingPage()">
            <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-gov-blue to-gov-teal flex items-center justify-center shadow-md border border-cyan-400/40 shrink-0">
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path>
              </svg>
            </div>
            <div>
              <span class="text-sm font-extrabold tracking-tight text-white block">AICTE COMPLAINT ENCLAVE</span>
              <span class="text-[10px] text-cyan-200 font-semibold" id="activePortalIndicator">Regulation Bureau (RB)</span>
            </div>
          </div>

          <!-- Main Tab Navigation -->
          <div class="hidden md:flex items-center space-x-1 text-xs font-bold text-slate-300">
            <button onclick="switchTab('dashboard')" id="nav-tab-dashboard" class="px-3.5 py-2 rounded-lg hover:text-white hover:bg-slate-800 transition-colors tab-active">
              Overview
            </button>
            <button onclick="switchTab('complaints')" id="nav-tab-complaints" class="px-3.5 py-2 rounded-lg hover:text-white hover:bg-slate-800 transition-colors">
              Complaints Dossier
            </button>
            <button onclick="switchTab('overlap')" id="nav-tab-overlap" class="px-3.5 py-2 rounded-lg hover:text-white hover:bg-slate-800 transition-colors flex items-center gap-1.5">
              <span>Overlap Engine</span>
              <span class="bg-rose-500 text-white text-[9px] px-1.5 py-0.2 rounded-full font-black animate-pulse">2</span>
            </button>
            <button onclick="switchTab('institutions')" id="nav-tab-institutions" class="px-3.5 py-2 rounded-lg hover:text-white hover:bg-slate-800 transition-colors">
              Institutions
            </button>
            <button onclick="switchTab('reports')" id="nav-tab-reports" class="px-3.5 py-2 rounded-lg hover:text-white hover:bg-slate-800 transition-colors">
              Analytics &amp; Reports
            </button>
            <button onclick="switchTab('users')" id="nav-tab-users" class="hidden px-3.5 py-2 rounded-lg hover:text-white hover:bg-slate-800 transition-colors text-amber-300">
              Admin Governance
            </button>
          </div>

          <!-- Right Controls: Role Switcher Dropdown, Notifications, Profile -->
          <div class="flex items-center gap-3">
            
            <!-- Notifications Bell -->
            <div class="relative">
              <button onclick="toggleNotifDropdown(event)" class="p-2 rounded-xl text-slate-300 hover:text-white hover:bg-slate-800 transition-colors relative">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path></svg>
                <span id="notifBadge" class="absolute top-1 right-1 w-2 h-2 rounded-full bg-rose-500"></span>
              </button>
              
              <!-- Dropdown Panel -->
              <div id="notifDropdown" class="hidden absolute right-0 mt-2 w-80 bg-white rounded-2xl shadow-2xl border border-slate-200 z-50 text-xs text-slate-800 overflow-hidden">
                <div class="bg-gov-navy text-white px-4 py-2.5 flex items-center justify-between">
                  <span class="font-bold">System Alerts &amp; Directives</span>
                  <span class="text-[10px] text-cyan-200 font-mono">Real-Time</span>
                </div>
                <div id="notifList" class="divide-y divide-slate-100 max-h-72 overflow-y-auto">
                  <!-- Populated by JS -->
                </div>
              </div>
            </div>

            <!-- Role Selector Slide-Down Dropdown -->
            <div class="relative" id="customRoleDropdownContainer">
              <button type="button" id="roleDropdownTrigger" onclick="toggleRoleDropdown(event)" class="flex items-center gap-2 bg-slate-800/90 hover:bg-slate-700/90 border border-slate-600 px-3 py-1.5 rounded-xl transition-all shadow-sm">
                <div class="w-6 h-6 rounded-lg bg-gov-teal text-white flex items-center justify-center font-bold text-[10px]" id="userAvatar">
                  RB
                </div>
                <div class="text-left hidden sm:block">
                  <div class="text-[11px] font-extrabold text-white leading-tight" id="userNameDisplay">Dr. Arvind Joshi</div>
                  <div class="text-[9px] text-cyan-200 font-medium" id="userRoleDisplay">Regulation Bureau (RB)</div>
                </div>
                <svg id="triggerChevron" class="w-3.5 h-3.5 text-slate-400 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
              </button>

              <!-- Slide Down Menu for 7 Roles -->
              <div id="roleDropdownMenu" class="hidden absolute right-0 mt-2 w-72 bg-white rounded-2xl shadow-2xl border border-slate-200 z-50 p-2 space-y-1 text-xs text-slate-800">
                <div class="px-3 py-1.5 text-[10px] font-black uppercase tracking-wider text-slate-400 border-b border-slate-100">
                  Switch Active Portal Role (7 Roles)
                </div>
                <button onclick="selectRoleOption('rb_officer')" class="w-full text-left px-3 py-2 rounded-xl hover:bg-blue-50 flex items-center gap-2.5 transition-colors">
                  <div class="w-6 h-6 rounded-lg bg-blue-600 text-white flex items-center justify-center font-bold text-[10px]">RB</div>
                  <div>
                    <div class="font-bold text-blue-900">1. Regulation Bureau (RB)</div>
                    <div class="text-[10px] text-slate-500">Dr. Arvind Joshi &bull; Director</div>
                  </div>
                </button>
                <button onclick="selectRoleOption('pgrc_officer')" class="w-full text-left px-3 py-2 rounded-xl hover:bg-purple-50 flex items-center gap-2.5 transition-colors">
                  <div class="w-6 h-6 rounded-lg bg-purple-600 text-white flex items-center justify-center font-bold text-[10px]">PG</div>
                  <div>
                    <div class="font-bold text-purple-900">2. Public Grievance Cell (PGRC)</div>
                    <div class="text-[10px] text-slate-500">Smt. Sunita Sharma &bull; Dy Director</div>
                  </div>
                </button>
                <button onclick="selectRoleOption('admin')" class="w-full text-left px-3 py-2 rounded-xl hover:bg-slate-100 flex items-center gap-2.5 transition-colors">
                  <div class="w-6 h-6 rounded-lg bg-slate-800 text-white flex items-center justify-center font-bold text-[10px]">AD</div>
                  <div>
                    <div class="font-bold text-slate-900">3. System Administrator</div>
                    <div class="text-[10px] text-slate-500">Full Access &amp; User Provisioning</div>
                  </div>
                </button>
                <button onclick="selectRoleOption('ro_officer')" class="w-full text-left px-3 py-2 rounded-xl hover:bg-emerald-50 flex items-center gap-2.5 transition-colors">
                  <div class="w-6 h-6 rounded-lg bg-emerald-600 text-white flex items-center justify-center font-bold text-[10px]">RO</div>
                  <div>
                    <div class="font-bold text-emerald-900">4. Regional Officer (WRO)</div>
                    <div class="text-[10px] text-slate-500">Western Region &bull; Mumbai HQ</div>
                  </div>
                </button>
                <button onclick="selectRoleOption('senior_mgmt')" class="w-full text-left px-3 py-2 rounded-xl hover:bg-amber-50 flex items-center gap-2.5 transition-colors">
                  <div class="w-6 h-6 rounded-lg bg-amber-600 text-slate-950 flex items-center justify-center font-black text-[10px]">MS</div>
                  <div>
                    <div class="font-bold text-amber-900">5. Senior Management</div>
                    <div class="text-[10px] text-slate-500">Council Secretariat &bull; Advisor</div>
                  </div>
                </button>
                <button onclick="selectRoleOption('college_inst')" class="w-full text-left px-3 py-2 rounded-xl hover:bg-cyan-50 flex items-center gap-2.5 transition-colors">
                  <div class="w-6 h-6 rounded-lg bg-cyan-600 text-white flex items-center justify-center font-bold text-[10px]">CI</div>
                  <div>
                    <div class="font-bold text-cyan-900">6. College / Institution</div>
                    <div class="text-[10px] text-slate-500">Apex Institute &bull; Principal</div>
                  </div>
                </button>
                <button onclick="selectRoleOption('university')" class="w-full text-left px-3 py-2 rounded-xl hover:bg-indigo-50 flex items-center gap-2.5 transition-colors">
                  <div class="w-6 h-6 rounded-lg bg-indigo-600 text-white flex items-center justify-center font-bold text-[10px]">UN</div>
                  <div>
                    <div class="font-bold text-indigo-900">7. University Authority</div>
                    <div class="text-[10px] text-slate-500">State Technical University</div>
                  </div>
                </button>
                <div class="pt-1 border-t border-slate-100 flex justify-between items-center text-[10px]">
                  <button onclick="handleLogout()" class="text-rose-600 hover:underline font-bold px-3 py-1">Log Out</button>
                  <button onclick="showLandingPage()" class="text-gov-lightBlue hover:underline font-bold px-3 py-1">Home Page</button>
                </div>
              </div>
            </div>

            <!-- Log Out Button -->
            <button onclick="handleLogout()" class="p-2 rounded-xl text-slate-300 hover:text-white hover:bg-slate-800 transition-colors" title="Log Out">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path></svg>
            </button>

          </div>

        </div>
      </div>
    </nav>

    <!-- Main Dynamic View Container -->
    <main class="flex-1 overflow-y-auto bg-slate-50 p-4 sm:p-6 lg:p-8 space-y-6">
      
      <!-- Role Workspace Top Banner -->
      <div id="roleWorkspaceBanner" class="bg-gradient-to-r from-gov-navy to-gov-blue text-white p-5 rounded-2xl shadow-card border border-blue-900/60 flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div class="flex items-center gap-2">
            <span class="bg-gov-teal text-white text-[10px] font-black uppercase px-2 py-0.5 rounded tracking-wider" id="roleBadgeDisplay">
              Regulation Bureau (RB) Officer
            </span>
            <span class="text-xs text-cyan-200 font-mono" id="roleAicteIdDisplay">GOV-RB-01</span>
          </div>
          <h2 class="text-xl font-extrabold text-white mt-1" id="roleBannerTitle">
            Regulation Bureau (RB) Regulatory Oversight
          </h2>
          <p class="text-xs text-slate-300 mt-1" id="roleBannerDesc">
            Monitoring technical institutions for regulatory compliance, 7th CPC norms, unapproved seats, and coordination with PGRC.
          </p>
        </div>
        <div class="flex items-center gap-2 shrink-0">
          <button onclick="openComplaintWizard()" class="px-4 py-2 bg-amber-400 hover:bg-amber-300 text-slate-950 font-black rounded-xl text-xs flex items-center gap-1.5 shadow-sm">
            <svg class="w-4 h-4 text-slate-950" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 4v16m8-8H4"></path></svg>
            <span>Lodge New Case</span>
          </button>
          <button onclick="runOverlapScan()" class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-white font-bold rounded-xl text-xs border border-slate-600 flex items-center gap-1.5 shadow-sm">
            <svg class="w-4 h-4 text-cyan-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
            <span>Scan Overlaps</span>
          </button>
        </div>
      </div>

      <!-- ========================================== -->
      <!-- TAB 1: DASHBOARD OVERVIEW -->
      <!-- ========================================== -->
      <section id="tab-content-dashboard" class="space-y-6">
        
        <!-- KPI Metrics Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm">
            <div class="text-xs font-bold text-slate-500 uppercase" id="kpiCard1Title">Total Active Cases</div>
            <div class="text-2xl font-black text-gov-navy mt-1 font-mono" id="kpiCard1Val">6</div>
            <div class="text-[11px] text-slate-400 mt-1" id="kpiCard1Sub">Across regulatory bureaus</div>
          </div>
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm">
            <div class="text-xs font-bold text-amber-700 uppercase" id="kpiCard2Title">Pending Inquiries</div>
            <div class="text-2xl font-black text-amber-600 mt-1 font-mono" id="kpiCard2Val">4</div>
            <div class="text-[11px] text-amber-700/80 mt-1" id="kpiCard2Sub">Under regulatory scrutiny</div>
          </div>
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm">
            <div class="text-xs font-bold text-rose-700 uppercase" id="kpiCard3Title">Overdue SLA Cases</div>
            <div class="text-2xl font-black text-rose-600 mt-1 font-mono" id="kpiCard3Val">2</div>
            <div class="text-[11px] text-rose-700/80 mt-1" id="kpiCard3Sub">Exceeded standard 30 days</div>
          </div>
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm">
            <div class="text-xs font-bold text-cyan-700 uppercase" id="kpiCard4Title">Identified Overlaps</div>
            <div class="text-2xl font-black text-cyan-600 mt-1 font-mono" id="kpiCard4Val">2</div>
            <div class="text-[11px] text-cyan-700/80 mt-1" id="kpiCard4Sub">RB &bull; PGRC sync alerts</div>
          </div>
        </div>

        <!-- Overlap Alert Ribbon -->
        <div id="overlapAlertRibbon" class="bg-amber-50 border border-amber-300 rounded-2xl p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3 shadow-sm">
          <div class="flex items-start gap-3">
            <div class="w-8 h-8 rounded-xl bg-amber-500 text-white flex items-center justify-center shrink-0 mt-0.5">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
            </div>
            <div>
              <div class="font-extrabold text-amber-900 text-xs">Concurrent Inter-Bureau Proceedings Detected</div>
              <p class="text-amber-800 text-[11px] mt-0.5">
                Apex Institute (1-3324567891) has simultaneous active inquiries in Regulation Bureau and PGRC.
              </p>
            </div>
          </div>
          <button onclick="switchTab('overlap')" class="px-4 py-2 bg-amber-500 hover:bg-amber-600 text-slate-950 font-black rounded-xl text-xs transition-colors shrink-0">
            Open Overlap Workspace &rarr;
          </button>
        </div>

        <!-- Dedicated Evidence Review Workspace (Section 8 Compliance) -->
        <div id="evidenceReviewWorkspace" class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm space-y-4">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-100 pb-3">
            <div>
              <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-purple-600"></span>
                <h3 class="text-sm font-extrabold text-gov-navy uppercase tracking-wider">
                  Evidence Scrutiny &amp; Hive AI Forensic Workspace
                </h3>
              </div>
              <p class="text-xs text-slate-500 mt-0.5">
                Inspect evidence attachments across assigned cases, verify Hive AI synthetic image signals, and record review decisions.
              </p>
            </div>
            <div class="text-[10px] font-mono bg-purple-50 text-purple-800 border border-purple-200 px-2.5 py-1 rounded-lg">
              Model: hive-ai-generated-image-detection-v2
            </div>
          </div>

          <!-- Evidence Items Table -->
          <div class="border border-slate-200 rounded-xl overflow-hidden">
            <table class="w-full text-left text-xs">
              <thead class="bg-slate-100 text-slate-700 font-bold uppercase text-[10px]">
                <tr>
                  <th class="py-2.5 px-3">Target Case ID</th>
                  <th class="py-2.5 px-3">Institution</th>
                  <th class="py-2.5 px-3">Evidence File</th>
                  <th class="py-2.5 px-3">Screening Status</th>
                  <th class="py-2.5 px-3">Hive AI Signal</th>
                  <th class="py-2.5 px-3 text-right">Officer Decision</th>
                </tr>
              </thead>
              <tbody id="evidenceReviewTableBody" class="divide-y divide-slate-100">
                <!-- Dynamically populated -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- Recent Complaints Table -->
        <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm space-y-4">
          <div class="flex items-center justify-between border-b border-slate-100 pb-3">
            <div>
              <h3 class="text-sm font-extrabold text-gov-navy">Recent Inquiries &amp; Grievances</h3>
              <p class="text-xs text-slate-500 mt-0.5">Click any case row to inspect dossier, timeline, and documents.</p>
            </div>
            <button onclick="switchTab('complaints')" class="text-xs font-bold text-gov-lightBlue hover:underline">
              View All Cases &rarr;
            </button>
          </div>

          <div class="border border-slate-200 rounded-xl overflow-hidden">
            <table class="w-full text-left text-xs">
              <thead class="bg-slate-100 text-slate-700 font-bold uppercase text-[10px]">
                <tr>
                  <th class="py-2.5 px-3">Case Reference</th>
                  <th class="py-2.5 px-3">Target Institution</th>
                  <th class="py-2.5 px-3">Category</th>
                  <th class="py-2.5 px-3">Bureau</th>
                  <th class="py-2.5 px-3">Status</th>
                  <th class="py-2.5 px-3 text-right">Actions</th>
                </tr>
              </thead>
              <tbody id="recentComplaintsTableBody" class="divide-y divide-slate-100">
                <!-- Dynamically populated -->
              </tbody>
            </table>
          </div>
        </div>

      </section>

      <!-- ========================================== -->
      <!-- TAB 2: COMPLAINTS DOSSIER -->
      <!-- ========================================== -->
      <section id="tab-content-complaints" class="hidden space-y-6">
        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-4">
          
          <!-- Filter Controls -->
          <div class="grid grid-cols-1 sm:grid-cols-4 gap-3 text-xs">
            <div class="relative sm:col-span-2">
              <input type="text" id="complaintSearchInput" oninput="applyComplaintFilters()" placeholder="Search Case ID, institution, category, or keyword..." class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl pl-9 pr-3 py-2 text-slate-800 focus:outline-none focus:border-gov-teal">
              <svg class="w-4 h-4 text-slate-400 absolute left-3 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
            </div>
            <div>
              <select id="filterBureau" onchange="applyComplaintFilters()" class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl p-2 text-slate-800 font-semibold focus:outline-none focus:border-gov-teal">
                <option value="ALL">All AICTE Bureaus</option>
                <option value="Regulation Bureau (RB)">Regulation Bureau (RB)</option>
                <option value="Public Grievance Redressal Cell (PGRC)">PGRC</option>
                <option value="Approval Bureau (AB)">Approval Bureau (AB)</option>
              </select>
            </div>
            <div>
              <select id="filterStatus" onchange="applyComplaintFilters()" class="w-full text-xs bg-slate-50 border border-slate-300 rounded-xl p-2 text-slate-800 font-semibold focus:outline-none focus:border-gov-teal">
                <option value="ALL">All Statuses</option>
                <option value="Under Process">Under Process / Scrutiny</option>
                <option value="Pending">Pending Notice</option>
                <option value="Escalated">Escalated</option>
                <option value="Resolved">Resolved / Disposed</option>
              </select>
            </div>
          </div>

          <!-- All Complaints Table -->
          <div class="border border-slate-200 rounded-xl overflow-hidden">
            <table class="w-full text-left text-xs">
              <thead class="bg-slate-100 text-slate-700 font-bold uppercase text-[10px]">
                <tr>
                  <th class="py-3 px-3">Case ID</th>
                  <th class="py-3 px-3">Institution Name</th>
                  <th class="py-3 px-3">Category</th>
                  <th class="py-3 px-3">Bureau &amp; Officer</th>
                  <th class="py-3 px-3">KYC Status</th>
                  <th class="py-3 px-3">Status</th>
                  <th class="py-3 px-3 text-right">Actions</th>
                </tr>
              </thead>
              <tbody id="allComplaintsTableBody" class="divide-y divide-slate-100">
                <!-- Dynamically populated -->
              </tbody>
            </table>
          </div>

        </div>
      </section>

      <!-- ========================================== -->
      <!-- TAB 3: OVERLAP DETECTION ENGINE -->
      <!-- ========================================== -->
      <section id="tab-content-overlap" class="hidden space-y-6">
        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-4">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-100 pb-3">
            <div>
              <h3 class="text-base font-extrabold text-gov-navy">AI-Assisted Cross-Bureau Overlap Engine</h3>
              <p class="text-xs text-slate-500 mt-0.5">
                Spots concurrent proceedings across Regulation Bureau (RB) and PGRC to avoid duplicate inspections and coordinate hearings.
              </p>
            </div>
            <button onclick="runOverlapScan()" class="px-4 py-2 bg-gov-navy hover:bg-gov-darkNavy text-white font-bold rounded-xl text-xs flex items-center gap-1.5 shadow-sm">
              <svg class="w-4 h-4 text-cyan-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
              <span>Run Multi-Factor Scan</span>
            </button>
          </div>

          <!-- Overlap Pairs Grid -->
          <div id="overlapPairsContainer" class="space-y-4">
            <!-- Dynamically populated -->
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- TAB 4: INSTITUTIONS DOSSIER -->
      <!-- ========================================== -->
      <section id="tab-content-institutions" class="hidden space-y-6">
        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-4">
          <div class="border-b border-slate-100 pb-3">
            <h3 class="text-base font-extrabold text-gov-navy">Approved Technical Institutions Directory</h3>
            <p class="text-xs text-slate-500 mt-0.5">Search permanent IDs, regulatory sanctions, and inter-bureau complaint history.</p>
          </div>

          <div class="border border-slate-200 rounded-xl overflow-hidden">
            <table class="w-full text-left text-xs">
              <thead class="bg-slate-100 text-slate-700 font-bold uppercase text-[10px]">
                <tr>
                  <th class="py-3 px-3">Permanent ID</th>
                  <th class="py-3 px-3">Institution Name</th>
                  <th class="py-3 px-3">State / Region</th>
                  <th class="py-3 px-3">Approval Status</th>
                  <th class="py-3 px-3">Linked Cases</th>
                  <th class="py-3 px-3 text-right">Actions</th>
                </tr>
              </thead>
              <tbody id="institutionsTableBody" class="divide-y divide-slate-100">
                <!-- Dynamically populated -->
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- TAB 5: REPORTS & ANALYTICS -->
      <!-- ========================================== -->
      <section id="tab-content-reports" class="hidden space-y-6">
        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-100 pb-3">
            <div>
              <h3 class="text-base font-extrabold text-gov-navy">National Grievance Analytics &amp; Disposal Trends</h3>
              <p class="text-xs text-slate-500 mt-0.5">Interactive data visualizer powered by Chart.js.</p>
            </div>
            <button onclick="downloadExecutiveBriefingReport()" class="px-4 py-2 bg-gov-lightBlue hover:bg-blue-600 text-white font-bold rounded-xl text-xs flex items-center gap-1.5 shadow-sm">
              <svg class="w-4 h-4 text-cyan-200" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
              <span>Export Executive Brief (PDF/CSV)</span>
            </button>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="bg-slate-50 p-4 rounded-xl border border-slate-200">
              <h4 class="font-bold text-slate-800 text-xs uppercase mb-3">Complaints Distributed by Bureau</h4>
              <div class="h-64 flex items-center justify-center">
                <canvas id="bureauChart"></canvas>
              </div>
            </div>
            <div class="bg-slate-50 p-4 rounded-xl border border-slate-200">
              <h4 class="font-bold text-slate-800 text-xs uppercase mb-3">Complaints by Lifecycle Status</h4>
              <div class="h-64 flex items-center justify-center">
                <canvas id="statusChart"></canvas>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ========================================== -->
      <!-- TAB 6: ADMIN GOVERNANCE & ACCESS CONTROL -->
      <!-- ========================================== -->
      <section id="tab-content-users" class="hidden space-y-6">
        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-6">
          
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-100 pb-3">
            <div>
              <h3 class="text-base font-extrabold text-gov-navy">Administrator User &amp; Access Governance</h3>
              <p class="text-xs text-slate-500 mt-0.5">Manage user roles, verify pending registrations, and review system audit history.</p>
            </div>
            <span class="badge bg-slate-800 text-white font-mono text-xs">Admin Privilege Enclave</span>
          </div>

          <!-- Pending Approvals Queue -->
          <div class="space-y-3">
            <h4 class="font-bold text-slate-900 text-xs uppercase tracking-wider">Pending Registrations Approval Queue</h4>
            <div id="pendingApprovalsContainer" class="border border-slate-200 rounded-xl overflow-hidden">
              <!-- Dynamically populated -->
            </div>
          </div>

          <!-- Active Users Table -->
          <div class="space-y-3">
            <h4 class="font-bold text-slate-900 text-xs uppercase tracking-wider">System Users &amp; Role Assignments</h4>
            <div class="border border-slate-200 rounded-xl overflow-hidden">
              <table class="w-full text-left text-xs">
                <thead class="bg-slate-100 text-slate-700 font-bold uppercase text-[10px]">
                  <tr>
                    <th class="py-3 px-3">User &amp; Organization</th>
                    <th class="py-3 px-3">Role</th>
                    <th class="py-3 px-3">Contact</th>
                    <th class="py-3 px-3">Status</th>
                    <th class="py-3 px-3 text-right">Actions</th>
                  </tr>
                </thead>
                <tbody id="adminUsersTableBody" class="divide-y divide-slate-100">
                  <!-- Dynamically populated -->
                </tbody>
              </table>
            </div>
          </div>

          <!-- System Audit Trail Table -->
          <div class="space-y-3">
            <h4 class="font-bold text-slate-900 text-xs uppercase tracking-wider">System-Wide Audit Trail</h4>
            <div class="border border-slate-200 rounded-xl overflow-hidden">
              <table class="w-full text-left text-xs">
                <thead class="bg-slate-100 text-slate-700 font-bold uppercase text-[10px]">
                  <tr>
                    <th class="py-2.5 px-3">Timestamp</th>
                    <th class="py-2.5 px-3">Actor &amp; Role</th>
                    <th class="py-2.5 px-3">Action</th>
                    <th class="py-2.5 px-3">Target Reference</th>
                    <th class="py-2.5 px-3">Audit Details</th>
                  </tr>
                </thead>
                <tbody id="systemAuditLogsTableBody" class="divide-y divide-slate-100 font-mono text-[11px]">
                  <!-- Dynamically populated -->
                </tbody>
              </table>
            </div>
          </div>

        </div>
      </section>

    </main>
  </div>
'''
