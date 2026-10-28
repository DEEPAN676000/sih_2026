# -*- coding: utf-8 -*-
"""
Landing page section inspired by AICTE National Internship Portal (https://internship.aicte-india.org/)
Includes:
- Indian National Tricolor ribbon
- Top Government Identity Banner
- Sticky Institutional Navigation Header with AICTE seal and mobile menu
- Hero Section: "One Platform. Transparent Grievance Redressal." with 3 actions (Raise, Track, Access Portals)
- Public Tracking & Quick Verification Search Bar
- Statistics Section (5 KPI cards, labeled demonstration metrics)
- 6 Interactive Service Cards
- 7-Role Portal Access Section ("Access Your Portal")
- Complaint Redressal Workflow Lifecycle (7 visual stages)
- Official Institutional Footer
"""

def get_landing_html():
    return '''  <!-- ========================================== -->
  <!-- 1. LANDING PAGE / WELCOME SCREEN (DEFAULT VIEW) -->
  <!-- ========================================== -->
  <div id="landingPageScreen" class="min-h-screen bg-gov-surface flex flex-col z-30 relative">
    
    <!-- Top Indian National Tricolor Ribbon -->
    <div class="h-1.5 bg-gradient-to-r from-[#FF9933] via-white to-[#138808] shadow-sm"></div>

    <!-- Top Government Identity Banner -->
    <div class="bg-gov-darkNavy text-white border-b border-slate-800 text-xs px-4 sm:px-6 py-2 flex flex-wrap justify-between items-center">
      <div class="flex items-center gap-3">
        <span class="inline-flex items-center gap-1.5 font-semibold text-slate-300">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
          भारत सरकार | Government of India &bull; शिक्षा मंत्रालय | Ministry of Education
        </span>
        <span class="hidden md:inline text-slate-600">|</span>
        <span class="hidden md:inline text-slate-300">अखिल भारतीय तकनीकी शिक्षा परिषद (AICTE)</span>
      </div>
      <div class="flex items-center gap-4 text-slate-300">
        <span class="bg-gov-teal/20 text-cyan-300 border border-gov-teal/40 px-2.5 py-0.5 rounded font-mono font-bold text-[11px]">
          SIH 2026 EDITION
        </span>
        <div id="landingLiveClock" class="font-mono text-slate-300 text-[11px] hidden sm:block">--:--:-- IST</div>
        <button onclick="toggleHighContrast()" class="hover:text-white transition-colors text-[11px] flex items-center gap-1" title="Accessibility Mode">
          <span>A+</span>
        </button>
      </div>
    </div>

    <!-- Main Institutional Navigation Header (Inspired by AICTE National Portal) -->
    <header class="bg-gov-navy text-white shadow-lg border-b border-blue-900/60 sticky top-0 z-40">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 py-3 flex items-center justify-between">
        
        <!-- Council Emblem & Project Branding -->
        <a href="javascript:void(0)" onclick="showLandingPage()" class="flex items-center gap-3.5 group">
          <div class="w-12 h-12 rounded-xl bg-gradient-to-tr from-gov-blue to-gov-teal flex items-center justify-center shadow-md border border-cyan-400/30 shrink-0 group-hover:scale-105 transition-transform">
            <!-- AICTE Seal Icon -->
            <svg class="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path>
            </svg>
          </div>
          <div>
            <div class="flex items-center gap-2">
              <span class="text-sm sm:text-base font-extrabold tracking-tight text-white uppercase">
                All India Council for Technical Education
              </span>
              <span class="bg-amber-400 text-slate-950 text-[10px] font-black uppercase px-1.5 py-0.5 rounded shadow-sm">AICTE</span>
            </div>
            <p class="text-xs text-cyan-200 font-semibold tracking-wide">Institution Complaint Monitoring System (SIH 2026)</p>
          </div>
        </a>

        <!-- Desktop Navigation Menu -->
        <nav class="hidden lg:flex items-center gap-6 text-xs font-semibold text-slate-200">
          <a href="javascript:void(0)" onclick="showLandingPage()" class="text-white hover:text-cyan-300 transition-colors">Home</a>
          <a href="javascript:void(0)" onclick="openAboutModal()" class="hover:text-cyan-300 transition-colors">About System</a>
          <a href="javascript:void(0)" onclick="showPublicTrackModal()" class="hover:text-cyan-300 transition-colors">Track Complaint</a>
          <a href="javascript:void(0)" onclick="openInstitutionsDirectoryModal()" class="hover:text-cyan-300 transition-colors">Institutions</a>
          <a href="javascript:void(0)" onclick="openHelpModal()" class="hover:text-cyan-300 transition-colors">Help &amp; Support</a>
        </nav>

        <!-- Right Action Buttons (The 3 Primary Actions) -->
        <div class="flex items-center gap-2 sm:gap-3">
          <button onclick="showLoginModal()" class="px-3.5 py-2 rounded-xl text-xs font-bold text-white bg-slate-800 hover:bg-slate-700 border border-slate-600 transition-all shadow-sm flex items-center gap-1.5">
            <svg class="w-4 h-4 text-cyan-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"></path></svg>
            <span>Log In</span>
          </button>
          
          <button onclick="showRegisterModal()" class="px-3.5 py-2 rounded-xl text-xs font-bold text-white bg-gov-lightBlue hover:bg-blue-600 transition-all shadow-sm flex items-center gap-1.5">
            <svg class="w-4 h-4 text-cyan-200" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"></path></svg>
            <span>Register</span>
          </button>

          <button onclick="openComplaintWizard()" class="px-4 py-2 rounded-xl text-xs font-black text-gov-darkNavy bg-gradient-to-r from-gov-teal to-cyan-300 hover:from-cyan-300 hover:to-gov-teal transition-all shadow-glow-teal flex items-center gap-1.5">
            <svg class="w-4 h-4 text-gov-darkNavy" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 4v16m8-8H4"></path></svg>
            <span>Raise a Complaint</span>
          </button>

          <!-- Mobile Hamburger Menu Button -->
          <button onclick="toggleMobileNav()" class="lg:hidden p-2 rounded-lg bg-slate-800 text-white hover:bg-slate-700">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path></svg>
          </button>
        </div>

      </div>

      <!-- Mobile Navigation Drawer -->
      <div id="mobileNavMenu" class="hidden lg:hidden bg-gov-darkNavy border-t border-slate-800 px-4 py-3 space-y-2 text-xs font-semibold">
        <a href="javascript:void(0)" onclick="showLandingPage(); toggleMobileNav();" class="block py-1.5 text-white">Home</a>
        <a href="javascript:void(0)" onclick="openAboutModal(); toggleMobileNav();" class="block py-1.5 text-slate-300 hover:text-white">About System</a>
        <a href="javascript:void(0)" onclick="showPublicTrackModal(); toggleMobileNav();" class="block py-1.5 text-slate-300 hover:text-white">Track Complaint</a>
        <a href="javascript:void(0)" onclick="openInstitutionsDirectoryModal(); toggleMobileNav();" class="block py-1.5 text-slate-300 hover:text-white">Institutions</a>
        <a href="javascript:void(0)" onclick="openHelpModal(); toggleMobileNav();" class="block py-1.5 text-slate-300 hover:text-white">Help &amp; Support</a>
        <a href="javascript:void(0)" onclick="scrollToSection('accessPortalsSection'); toggleMobileNav();" class="block py-1.5 text-cyan-300 hover:text-white">7 Stakeholder Portals</a>
      </div>
    </header>

    <!-- Hero Section -->
    <section class="bg-gradient-to-br from-gov-darkNavy via-gov-navy to-slate-900 text-white py-16 px-4 sm:px-6 lg:px-8 border-b border-blue-900/60 relative overflow-hidden">
      <!-- Background subtle emblem watermark -->
      <div class="absolute -right-16 -bottom-16 opacity-5 pointer-events-none">
        <svg class="w-96 h-96 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2L1 21h22L12 2zm0 3.99L19.53 19H4.47L12 5.99zM11 10h2v4h-2zm0 6h2v2h-2z"/></svg>
      </div>

      <div class="max-w-7xl mx-auto relative z-10">
        
        <div class="inline-flex items-center gap-2 bg-gov-teal/20 border border-cyan-400/40 text-cyan-200 px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider mb-4">
          <span class="w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span>
          CENTRALIZED GRIEVANCE &amp; REGULATORY REDRESSAL ENCLAVE
        </div>

        <h1 class="text-3xl sm:text-5xl font-extrabold tracking-tight text-white max-w-4xl leading-tight">
          One Platform. Transparent Grievance Redressal.
        </h1>
        
        <p class="text-slate-300 text-sm sm:text-base max-w-3xl mt-4 leading-relaxed font-normal">
          A centralized platform for monitoring institutional complaints, coordinating AICTE bureaus, identifying overlapping cases, and improving grievance resolution transparency across the Regulation Bureau (RB), Public Grievance Redressal Cell (PGRC), and Regional Offices.
        </p>

        <!-- Working Actions Banner -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-5 mt-10 max-w-5xl">
          
          <!-- Action 1: Raise a Complaint -->
          <div class="bg-gradient-to-br from-amber-500/20 to-gov-navy/80 hover:from-amber-500/30 backdrop-blur-md rounded-2xl p-6 border border-amber-400/40 hover:border-amber-400 transition-all flex flex-col justify-between group shadow-xl">
            <div>
              <div class="w-12 h-12 rounded-xl bg-amber-500/20 text-amber-300 border border-amber-400/30 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
              </div>
              <div class="text-[10px] font-bold tracking-wider uppercase text-amber-300">Action 1</div>
              <h3 class="text-lg font-black text-white mt-1">Raise a Complaint</h3>
              <p class="text-xs text-slate-300 mt-2 leading-relaxed">
                6-step submission wizard with mandatory DigiLocker/Aadhaar KYC identity verification and Hive AI evidence image screening.
              </p>
            </div>
            <button onclick="openComplaintWizard()" class="mt-6 w-full py-2.5 px-4 rounded-xl bg-amber-400 hover:bg-amber-300 text-slate-950 font-black text-xs transition-colors flex items-center justify-center gap-2 shadow-glow-amber">
              <span>Start Submission Wizard</span>
              <svg class="w-4 h-4 text-slate-950" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
            </button>
          </div>

          <!-- Action 2: Track a Complaint -->
          <div class="bg-white/10 hover:bg-white/15 backdrop-blur-md rounded-2xl p-6 border border-white/10 hover:border-cyan-400/50 transition-all flex flex-col justify-between group shadow-xl">
            <div>
              <div class="w-12 h-12 rounded-xl bg-cyan-500/20 text-cyan-300 border border-cyan-400/30 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
              </div>
              <div class="text-[10px] font-bold tracking-wider uppercase text-cyan-300">Action 2</div>
              <h3 class="text-lg font-black text-white mt-1">Track a Complaint</h3>
              <p class="text-xs text-slate-300 mt-2 leading-relaxed">
                Check chronological inquiry stages, assigned bureau, SLA target, and disposal status using your AICTE Case ID.
              </p>
            </div>
            <button onclick="showPublicTrackModal()" class="mt-6 w-full py-2.5 px-4 rounded-xl bg-gov-teal hover:bg-cyan-300 text-gov-darkNavy font-black text-xs transition-colors flex items-center justify-center gap-2 shadow-md">
              <span>Public Tracking Desk</span>
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
            </button>
          </div>

          <!-- Action 3: Access Officer Portals -->
          <div class="bg-white/10 hover:bg-white/15 backdrop-blur-md rounded-2xl p-6 border border-white/10 hover:border-blue-400/50 transition-all flex flex-col justify-between group shadow-xl">
            <div>
              <div class="w-12 h-12 rounded-xl bg-blue-500/20 text-blue-300 border border-blue-400/30 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
              </div>
              <div class="text-[10px] font-bold tracking-wider uppercase text-blue-300">Action 3</div>
              <h3 class="text-lg font-black text-white mt-1">Access Officer Portals</h3>
              <p class="text-xs text-slate-300 mt-2 leading-relaxed">
                Dedicated workspaces for Regulation Bureau, PGRC, Administrators, Western Regional Office, Senior Management, and Institutions.
              </p>
            </div>
            <button onclick="scrollToSection('accessPortalsSection')" class="mt-6 w-full py-2.5 px-4 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-black text-xs transition-colors flex items-center justify-center gap-2 shadow-md">
              <span>View 7 Stakeholder Portals</span>
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7"></path></svg>
            </button>
          </div>

        </div>

      </div>
    </section>

    <!-- Public Tracking & Quick Verification Bar -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full -mt-8 relative z-20">
      <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-card">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-3">
          <div>
            <span class="text-[10px] font-black uppercase tracking-wider text-gov-lightBlue bg-blue-50 px-2 py-0.5 rounded">
              Public Tracking &amp; Verification Desk
            </span>
            <h2 class="text-lg font-black text-gov-navy mt-1">Track Case Progress or Verify Approved Institution</h2>
          </div>
          <div class="text-xs text-slate-500 flex items-center gap-2">
            <span>Quick test:</span>
            <button type="button" onclick="document.getElementById('quickSearchInput').value='AICTE/RB/2026/0104'; executeQuickSearch();" class="text-gov-lightBlue font-bold hover:underline font-mono bg-slate-100 px-2 py-0.5 rounded">
              AICTE/RB/2026/0104
            </button>
          </div>
        </div>

        <form onsubmit="handleQuickSearchSubmit(event)" class="flex flex-col sm:flex-row gap-3">
          <div class="relative flex-1">
            <input type="text" id="quickSearchInput" placeholder="Enter AICTE Case ID (e.g. AICTE/RB/2026/0104) or Institution Permanent ID (1-3324567891)..." required class="w-full text-xs font-mono bg-slate-50 border border-slate-300 rounded-xl pl-10 pr-4 py-3 text-slate-800 focus:outline-none focus:border-gov-teal">
            <svg class="w-4 h-4 text-slate-400 absolute left-3.5 top-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
          </div>
          <button type="submit" class="bg-gov-navy hover:bg-gov-darkNavy text-white font-bold px-6 py-3 rounded-xl text-xs flex items-center justify-center gap-2 transition-all shadow-md shrink-0">
            <span>Search Records</span>
            <svg class="w-4 h-4 text-cyan-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
          </button>
        </form>
      </div>
    </section>

    <!-- Statistics Section (Requirement C) -->
    <section class="py-12 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto w-full">
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-6">
        <div>
          <span class="text-[10px] font-black uppercase tracking-wider text-gov-teal bg-teal-50 px-2 py-0.5 rounded border border-teal-200">
            Live System Statistics
          </span>
          <h3 class="text-2xl font-black text-gov-navy mt-1 tracking-tight">National Grievance Monitoring Metrics</h3>
        </div>
        <div class="text-[11px] font-semibold text-slate-400 mt-1 md:mt-0 italic">
          * Demonstration Metrics &bull; Powered by local SIH simulation data
        </div>
      </div>

      <div class="grid grid-cols-2 md:grid-cols-5 gap-4">
        <!-- Metric 1: Total Complaints -->
        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm hover:shadow-card transition-all text-center sm:text-left">
          <div class="text-xs font-bold text-slate-500 uppercase">Total Complaints</div>
          <div class="text-3xl font-black text-gov-navy mt-2 font-mono" id="statTotalComplaints">6</div>
          <div class="text-[11px] text-slate-400 mt-1">Across all bureaus</div>
        </div>

        <!-- Metric 2: Pending Complaints -->
        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm hover:shadow-card transition-all text-center sm:text-left">
          <div class="text-xs font-bold text-amber-700 uppercase">Pending Complaints</div>
          <div class="text-3xl font-black text-amber-600 mt-2 font-mono" id="statPendingComplaints">4</div>
          <div class="text-[11px] text-amber-700/80 mt-1">Active regulatory inquiry</div>
        </div>

        <!-- Metric 3: Resolved Complaints -->
        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm hover:shadow-card transition-all text-center sm:text-left">
          <div class="text-xs font-bold text-emerald-700 uppercase">Resolved Cases</div>
          <div class="text-3xl font-black text-emerald-600 mt-2 font-mono" id="statResolvedComplaints">1</div>
          <div class="text-[11px] text-emerald-700/80 mt-1">Disposed with restitution</div>
        </div>

        <!-- Metric 4: Institutions Registered -->
        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm hover:shadow-card transition-all text-center sm:text-left">
          <div class="text-xs font-bold text-blue-700 uppercase">Institutions Tracked</div>
          <div class="text-3xl font-black text-blue-600 mt-2 font-mono" id="statInstitutionsCount">5</div>
          <div class="text-[11px] text-blue-700/80 mt-1">AICTE approved colleges</div>
        </div>

        <!-- Metric 5: Overlapping Complaints Detected -->
        <div class="bg-white p-5 rounded-2xl border border-rose-200 bg-rose-50/30 shadow-sm hover:shadow-card transition-all text-center sm:text-left col-span-2 md:col-span-1">
          <div class="text-xs font-bold text-rose-700 uppercase">Overlaps Detected</div>
          <div class="text-3xl font-black text-rose-600 mt-2 font-mono" id="statOverlapsCount">2</div>
          <div class="text-[11px] text-rose-700/80 mt-1">RB &bull; PGRC synchronized</div>
        </div>
      </div>
    </section>

    <!-- Service Cards Section (Requirement D: 6 Interactive Cards) -->
    <section class="py-8 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto w-full">
      <div class="text-center max-w-3xl mx-auto mb-8">
        <span class="text-[10px] font-black uppercase tracking-wider text-gov-lightBlue bg-blue-50 px-2 py-0.5 rounded">
          Platform Capabilities
        </span>
        <h3 class="text-2xl font-black text-gov-navy mt-1 tracking-tight">AICTE Redressal &amp; Governance Services</h3>
        <p class="text-xs text-slate-500 mt-2">Every service card connects to a working workflow, verification tool, or regulatory workspace.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        
        <!-- Card 1: Submit a Complaint -->
        <div onclick="openComplaintWizard()" class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm hover:shadow-card transition-all cursor-pointer group flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-xl bg-blue-50 text-gov-lightBlue flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path></svg>
            </div>
            <h4 class="font-bold text-slate-900 text-base group-hover:text-gov-lightBlue transition-colors">1. Submit a Complaint</h4>
            <p class="text-xs text-slate-500 mt-2 leading-relaxed">
              Launch the 6-step wizard with mandatory KYC verification, automatic bureau routing, and Hive AI image screening.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-100 flex items-center text-xs font-bold text-gov-lightBlue">
            <span>Launch Wizard &rarr;</span>
          </div>
        </div>

        <!-- Card 2: Track Complaint Status -->
        <div onclick="showPublicTrackModal()" class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm hover:shadow-card transition-all cursor-pointer group flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-xl bg-cyan-50 text-cyan-700 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path></svg>
            </div>
            <h4 class="font-bold text-slate-900 text-base group-hover:text-cyan-700 transition-colors">2. Track Complaint Status</h4>
            <p class="text-xs text-slate-500 mt-2 leading-relaxed">
              Real-time chronological timeline lookup for complainants with disposal SLA countdown without logging in.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-100 flex items-center text-xs font-bold text-cyan-700">
            <span>Check Status &rarr;</span>
          </div>
        </div>

        <!-- Card 3: Institution Verification -->
        <div onclick="openInstitutionsDirectoryModal()" class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm hover:shadow-card transition-all cursor-pointer group flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-xl bg-emerald-50 text-emerald-700 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
            </div>
            <h4 class="font-bold text-slate-900 text-base group-hover:text-emerald-700 transition-colors">3. Institution Verification</h4>
            <p class="text-xs text-slate-500 mt-2 leading-relaxed">
              Dossier lookup for AICTE Permanent IDs, approval status, active show-cause notices, and affiliated universities.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-100 flex items-center text-xs font-bold text-emerald-700">
            <span>Verify Institution &rarr;</span>
          </div>
        </div>

        <!-- Card 4: Evidence Review -->
        <div onclick="openEvidenceReviewFromLanding()" class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm hover:shadow-card transition-all cursor-pointer group flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-xl bg-purple-50 text-purple-700 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
            </div>
            <h4 class="font-bold text-slate-900 text-base group-hover:text-purple-700 transition-colors">4. Evidence Review</h4>
            <p class="text-xs text-slate-500 mt-2 leading-relaxed">
              Regulatory workspace for officers to inspect uploaded photos, examine Hive AI synthetic scores, and record decisions.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-100 flex items-center text-xs font-bold text-purple-700">
            <span>Explore Review Desk &rarr;</span>
          </div>
        </div>

        <!-- Card 5: Grievance Resolution -->
        <div onclick="openGuidelinesModal()" class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm hover:shadow-card transition-all cursor-pointer group flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-xl bg-amber-50 text-amber-700 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
            </div>
            <h4 class="font-bold text-slate-900 text-base group-hover:text-amber-700 transition-colors">5. Grievance Resolution</h4>
            <p class="text-xs text-slate-500 mt-2 leading-relaxed">
              Official regulatory framework under AICTE Act guidelines for Ombudsman hearings, fee refund mandates, and 7th CPC compliance.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-100 flex items-center text-xs font-bold text-amber-700">
            <span>View Framework &rarr;</span>
          </div>
        </div>

        <!-- Card 6: Bureau Coordination -->
        <div onclick="openBureauCoordinationGuide()" class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm hover:shadow-card transition-all cursor-pointer group flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-xl bg-rose-50 text-rose-700 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
            </div>
            <h4 class="font-bold text-slate-900 text-base group-hover:text-rose-700 transition-colors">6. Bureau Coordination</h4>
            <p class="text-xs text-slate-500 mt-2 leading-relaxed">
              Cross-bureau overlap detection linking Regulation Bureau (RB) and PGRC to prevent duplicate orders and coordinate inspections.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-100 flex items-center text-xs font-bold text-rose-700">
            <span>Learn Overlap Logic &rarr;</span>
          </div>
        </div>

      </div>
    </section>

    <!-- Seven-Role Access Section (Requirement E: Access Your Portal) -->
    <section id="accessPortalsSection" class="py-12 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto w-full">
      <div class="text-center max-w-3xl mx-auto mb-10">
        <span class="text-[10px] font-black uppercase tracking-wider text-amber-600 bg-amber-50 border border-amber-200 px-3 py-1 rounded-full">
          Enterprise Access Control
        </span>
        <h3 class="text-3xl font-black text-gov-navy mt-2 tracking-tight">Access Your Portal</h3>
        <p class="text-xs text-slate-500 mt-2 leading-relaxed">
          Seven genuinely distinct, role-specific portals with specialized data permissions, action tools, and confidential workspaces. Click any card to enter that portal.
        </p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        
        <!-- Portal 1: RB Officer -->
        <div onclick="navigateToRoute('/portal/rb')" class="bg-white p-5 rounded-2xl border border-blue-200 shadow-sm hover:shadow-card hover:border-blue-500 transition-all cursor-pointer group flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="text-[10px] font-black uppercase px-2 py-0.5 rounded bg-blue-100 text-blue-900">Portal 1</span>
              <span class="text-xs text-slate-400 font-mono">/portal/rb</span>
            </div>
            <div class="w-10 h-10 rounded-xl bg-blue-600 text-white flex items-center justify-center font-bold text-sm mb-3 group-hover:scale-105 transition-transform">
              RB
            </div>
            <h4 class="font-extrabold text-slate-900 text-sm group-hover:text-blue-700">Regulation Bureau (RB)</h4>
            <p class="text-xs text-slate-500 mt-1.5 leading-relaxed">
              Statutory norm violations, 7th CPC faculty salaries, ghost faculty scrutiny, and inspection hearings.
            </p>
          </div>
          <button class="mt-4 w-full py-2 bg-blue-50 hover:bg-blue-600 hover:text-white text-blue-900 font-bold text-xs rounded-xl transition-colors flex items-center justify-center gap-1">
            <span>Enter RB Portal</span> &rarr;
          </button>
        </div>

        <!-- Portal 2: PGRC Officer -->
        <div onclick="navigateToRoute('/portal/pgrc')" class="bg-white p-5 rounded-2xl border border-purple-200 shadow-sm hover:shadow-card hover:border-purple-500 transition-all cursor-pointer group flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="text-[10px] font-black uppercase px-2 py-0.5 rounded bg-purple-100 text-purple-900">Portal 2</span>
              <span class="text-xs text-slate-400 font-mono">/portal/pgrc</span>
            </div>
            <div class="w-10 h-10 rounded-xl bg-purple-600 text-white flex items-center justify-center font-bold text-sm mb-3 group-hover:scale-105 transition-transform">
              PG
            </div>
            <h4 class="font-extrabold text-slate-900 text-sm group-hover:text-purple-700">Public Grievance Cell (PGRC)</h4>
            <p class="text-xs text-slate-500 mt-1.5 leading-relaxed">
              Student &amp; faculty grievances, degree certificate withholding, capitation fees, and Ombudsman directives.
            </p>
          </div>
          <button class="mt-4 w-full py-2 bg-purple-50 hover:bg-purple-600 hover:text-white text-purple-900 font-bold text-xs rounded-xl transition-colors flex items-center justify-center gap-1">
            <span>Enter PGRC Portal</span> &rarr;
          </button>
        </div>

        <!-- Portal 3: Admin Portal -->
        <div onclick="navigateToRoute('/portal/admin')" class="bg-white p-5 rounded-2xl border border-slate-300 shadow-sm hover:shadow-card hover:border-slate-700 transition-all cursor-pointer group flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="text-[10px] font-black uppercase px-2 py-0.5 rounded bg-slate-200 text-slate-900">Portal 3</span>
              <span class="text-xs text-slate-400 font-mono">/portal/admin</span>
            </div>
            <div class="w-10 h-10 rounded-xl bg-slate-800 text-white flex items-center justify-center font-bold text-sm mb-3 group-hover:scale-105 transition-transform">
              AD
            </div>
            <h4 class="font-extrabold text-slate-900 text-sm group-hover:text-slate-800">System Administrator</h4>
            <p class="text-xs text-slate-500 mt-1.5 leading-relaxed">
              User account management, privilege assignment, institution approvals, and immutable system audit trail.
            </p>
          </div>
          <button class="mt-4 w-full py-2 bg-slate-100 hover:bg-slate-800 hover:text-white text-slate-800 font-bold text-xs rounded-xl transition-colors flex items-center justify-center gap-1">
            <span>Enter Admin Portal</span> &rarr;
          </button>
        </div>

        <!-- Portal 4: Regional Officer -->
        <div onclick="navigateToRoute('/portal/regional')" class="bg-white p-5 rounded-2xl border border-emerald-200 shadow-sm hover:shadow-card hover:border-emerald-500 transition-all cursor-pointer group flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="text-[10px] font-black uppercase px-2 py-0.5 rounded bg-emerald-100 text-emerald-900">Portal 4</span>
              <span class="text-xs text-slate-400 font-mono">/portal/regional</span>
            </div>
            <div class="w-10 h-10 rounded-xl bg-emerald-600 text-white flex items-center justify-center font-bold text-sm mb-3 group-hover:scale-105 transition-transform">
              RO
            </div>
            <h4 class="font-extrabold text-slate-900 text-sm group-hover:text-emerald-700">Regional Officer (WRO)</h4>
            <p class="text-xs text-slate-500 mt-1.5 leading-relaxed">
              Region-restricted dashboard (Western Region), physical inspection logs, and regional follow-up notices.
            </p>
          </div>
          <button class="mt-4 w-full py-2 bg-emerald-50 hover:bg-emerald-600 hover:text-white text-emerald-900 font-bold text-xs rounded-xl transition-colors flex items-center justify-center gap-1">
            <span>Enter WRO Portal</span> &rarr;
          </button>
        </div>

        <!-- Portal 5: Senior Management -->
        <div onclick="navigateToRoute('/portal/management')" class="bg-white p-5 rounded-2xl border border-amber-200 shadow-sm hover:shadow-card hover:border-amber-500 transition-all cursor-pointer group flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="text-[10px] font-black uppercase px-2 py-0.5 rounded bg-amber-100 text-amber-900">Portal 5</span>
              <span class="text-xs text-slate-400 font-mono">/portal/management</span>
            </div>
            <div class="w-10 h-10 rounded-xl bg-amber-600 text-slate-950 flex items-center justify-center font-black text-sm mb-3 group-hover:scale-105 transition-transform">
              MS
            </div>
            <h4 class="font-extrabold text-slate-900 text-sm group-hover:text-amber-700">Senior Management</h4>
            <p class="text-xs text-slate-500 mt-1.5 leading-relaxed">
              Council Secretariat overview, RB vs PGRC workload ratio, disposal time trends, and executive briefing reports.
            </p>
          </div>
          <button class="mt-4 w-full py-2 bg-amber-50 hover:bg-amber-600 hover:text-white text-amber-900 font-bold text-xs rounded-xl transition-colors flex items-center justify-center gap-1">
            <span>Enter Management Portal</span> &rarr;
          </button>
        </div>

        <!-- Portal 6: College / Institution -->
        <div onclick="navigateToRoute('/portal/institution')" class="bg-white p-5 rounded-2xl border border-cyan-200 shadow-sm hover:shadow-card hover:border-cyan-500 transition-all cursor-pointer group flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="text-[10px] font-black uppercase px-2 py-0.5 rounded bg-cyan-100 text-cyan-900">Portal 6</span>
              <span class="text-xs text-slate-400 font-mono">/portal/institution</span>
            </div>
            <div class="w-10 h-10 rounded-xl bg-cyan-600 text-white flex items-center justify-center font-bold text-sm mb-3 group-hover:scale-105 transition-transform">
              CI
            </div>
            <h4 class="font-extrabold text-slate-900 text-sm group-hover:text-cyan-700">College / Institution</h4>
            <p class="text-xs text-slate-500 mt-1.5 leading-relaxed">
              Institutional dossier, strictly private complaints list (Apex Institute), and compliance response submission.
            </p>
          </div>
          <button class="mt-4 w-full py-2 bg-cyan-50 hover:bg-cyan-600 hover:text-white text-cyan-900 font-bold text-xs rounded-xl transition-colors flex items-center justify-center gap-1">
            <span>Enter College Portal</span> &rarr;
          </button>
        </div>

        <!-- Portal 7: University -->
        <div onclick="navigateToRoute('/portal/university')" class="bg-white p-5 rounded-2xl border border-indigo-200 shadow-sm hover:shadow-card hover:border-indigo-500 transition-all cursor-pointer group flex flex-col justify-between col-span-1 sm:col-span-2 lg:col-span-2">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="text-[10px] font-black uppercase px-2 py-0.5 rounded bg-indigo-100 text-indigo-900">Portal 7</span>
              <span class="text-xs text-slate-400 font-mono">/portal/university</span>
            </div>
            <div class="flex items-center gap-3 mb-3">
              <div class="w-10 h-10 rounded-xl bg-indigo-600 text-white flex items-center justify-center font-bold text-sm shrink-0 group-hover:scale-105 transition-transform">
                UN
              </div>
              <div>
                <h4 class="font-extrabold text-slate-900 text-sm group-hover:text-indigo-700">University Authority Portal</h4>
                <p class="text-[11px] text-slate-400">Affiliating University (State Technical University)</p>
              </div>
            </div>
            <p class="text-xs text-slate-500 leading-relaxed">
              Monitor grievance proceedings and regulatory orders across authorized affiliated colleges, upload university representations, and maintain affiliated college compliance matrices.
            </p>
          </div>
          <button class="mt-4 w-full py-2 bg-indigo-50 hover:bg-indigo-600 hover:text-white text-indigo-900 font-bold text-xs rounded-xl transition-colors flex items-center justify-center gap-1">
            <span>Enter University Portal</span> &rarr;
          </button>
        </div>

      </div>
    </section>

    <!-- Complaint Workflow Lifecycle (Requirement F) -->
    <section class="py-12 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto w-full border-t border-slate-200">
      <div class="text-center max-w-3xl mx-auto mb-10">
        <span class="text-[10px] font-black uppercase tracking-wider text-emerald-700 bg-emerald-50 border border-emerald-200 px-3 py-1 rounded-full">
          Workflow Architecture
        </span>
        <h3 class="text-2xl font-black text-gov-navy mt-2 tracking-tight">Complaint Redressal Lifecycle</h3>
        <p class="text-xs text-slate-500 mt-2">Every petition passes through seven transparent, accountable milestones.</p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-7 gap-3 text-center">
        
        <!-- Step 1 -->
        <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm flex flex-col justify-between">
          <div class="w-8 h-8 rounded-full bg-blue-100 text-gov-navy font-black text-xs mx-auto flex items-center justify-center mb-2">1</div>
          <div class="font-bold text-slate-900 text-xs">Complaint Submission</div>
          <p class="text-[11px] text-slate-500 mt-1">complainant details &amp; evidence intake</p>
        </div>

        <!-- Step 2 -->
        <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm flex flex-col justify-between">
          <div class="w-8 h-8 rounded-full bg-cyan-100 text-cyan-800 font-black text-xs mx-auto flex items-center justify-center mb-2">2</div>
          <div class="font-bold text-slate-900 text-xs">KYC Verification</div>
          <p class="text-[11px] text-slate-500 mt-1">DigiLocker / Aadhaar identity check</p>
        </div>

        <!-- Step 3 -->
        <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm flex flex-col justify-between">
          <div class="w-8 h-8 rounded-full bg-purple-100 text-purple-800 font-black text-xs mx-auto flex items-center justify-center mb-2">3</div>
          <div class="font-bold text-slate-900 text-xs">Evidence Screening</div>
          <p class="text-[11px] text-slate-500 mt-1">Hive AI synthetic image detection</p>
        </div>

        <!-- Step 4 -->
        <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm flex flex-col justify-between">
          <div class="w-8 h-8 rounded-full bg-amber-100 text-amber-800 font-black text-xs mx-auto flex items-center justify-center mb-2">4</div>
          <div class="font-bold text-slate-900 text-xs">Bureau Assignment</div>
          <p class="text-[11px] text-slate-500 mt-1">routed to RB, PGRC, or WRO</p>
        </div>

        <!-- Step 5 -->
        <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm flex flex-col justify-between">
          <div class="w-8 h-8 rounded-full bg-rose-100 text-rose-800 font-black text-xs mx-auto flex items-center justify-center mb-2">5</div>
          <div class="font-bold text-slate-900 text-xs">Investigation</div>
          <p class="text-[11px] text-slate-500 mt-1">show cause, hearing &amp; inspection</p>
        </div>

        <!-- Step 6 -->
        <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm flex flex-col justify-between">
          <div class="w-8 h-8 rounded-full bg-indigo-100 text-indigo-800 font-black text-xs mx-auto flex items-center justify-center mb-2">6</div>
          <div class="font-bold text-slate-900 text-xs">Resolution</div>
          <p class="text-[11px] text-slate-500 mt-1">restitution &amp; punitive directive</p>
        </div>

        <!-- Step 7 -->
        <div class="bg-white p-4 rounded-xl border border-emerald-200 bg-emerald-50/40 shadow-sm flex flex-col justify-between">
          <div class="w-8 h-8 rounded-full bg-emerald-100 text-emerald-800 font-black text-xs mx-auto flex items-center justify-center mb-2">7</div>
          <div class="font-bold text-emerald-900 text-xs">Closure</div>
          <p class="text-[11px] text-emerald-700/80 mt-1">verified audit disposal</p>
        </div>

      </div>
    </section>

    <!-- Official Institutional Footer (Requirement G) -->
    <footer class="mt-auto bg-gov-darkNavy text-slate-400 text-xs border-t border-slate-800 py-10 px-4 sm:px-6">
      <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-8 mb-8 text-[11px]">
        <div>
          <div class="font-bold text-white text-sm mb-2">All India Council for Technical Education</div>
          <p class="text-slate-400 leading-relaxed">
            Statutory body under the Ministry of Education, Government of India, regulating technical and management education institutions across the nation.
          </p>
        </div>
        <div>
          <div class="font-bold text-white text-xs uppercase mb-2">Platform Portals</div>
          <ul class="space-y-1.5">
            <li><a href="javascript:void(0)" onclick="navigateToRoute('/portal/rb')" class="hover:text-cyan-300">Regulation Bureau (RB)</a></li>
            <li><a href="javascript:void(0)" onclick="navigateToRoute('/portal/pgrc')" class="hover:text-cyan-300">Public Grievance Redressal Cell (PGRC)</a></li>
            <li><a href="javascript:void(0)" onclick="navigateToRoute('/portal/admin')" class="hover:text-cyan-300">System Administration</a></li>
            <li><a href="javascript:void(0)" onclick="navigateToRoute('/portal/regional')" class="hover:text-cyan-300">Western Regional Office (WRO)</a></li>
          </ul>
        </div>
        <div>
          <div class="font-bold text-white text-xs uppercase mb-2">Help &amp; Documentation</div>
          <ul class="space-y-1.5">
            <li><a href="javascript:void(0)" onclick="openAboutModal()" class="hover:text-cyan-300">About the System</a></li>
            <li><a href="javascript:void(0)" onclick="openHelpModal()" class="hover:text-cyan-300">Helpdesk &amp; FAQ</a></li>
            <li><a href="javascript:void(0)" onclick="openGuidelinesModal()" class="hover:text-cyan-300">AICTE Redressal Regulations</a></li>
            <li><a href="javascript:void(0)" onclick="showPublicTrackModal()" class="hover:text-cyan-300">Track Complaint Online</a></li>
          </ul>
        </div>
        <div>
          <div class="font-bold text-white text-xs uppercase mb-2">Official Contact &amp; Links</div>
          <p class="text-slate-400">Nelson Mandela Marg, Vasant Kunj, New Delhi - 110070</p>
          <p class="text-slate-300 font-semibold mt-1">Toll-Free Helpline: 1800-11-2323</p>
          <div class="mt-3 flex flex-wrap gap-2 text-[10px]">
            <a href="https://aicte-india.org" target="_blank" rel="noopener noreferrer" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded border border-slate-700">AICTE Official</a>
            <a href="https://thehive.ai" target="_blank" rel="noopener noreferrer" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-purple-300 rounded border border-slate-700">Hive AI</a>
          </div>
        </div>
      </div>

      <div class="max-w-7xl mx-auto pt-6 border-t border-slate-800/80 flex flex-col md:flex-row items-center justify-between gap-4 text-[11px]">
        <div>
          &copy; 2026 All India Council for Technical Education. Smart India Hackathon (SIH 2026) Project.
        </div>
        <div class="flex items-center gap-4 text-slate-400">
          <span>Terms of Use</span>
          <span>&bull;</span>
          <span>Privacy Policy</span>
          <span>&bull;</span>
          <span class="text-emerald-400 font-mono font-bold">NIC GovCloud Shield Active</span>
        </div>
      </div>
    </footer>

  </div>
'''
