import re

texto_prueba = '''[<li class="panel">
<a href="/"><span>Care Search</span></a>
<button data-parent="#accordion" data-toggle="collapse" href="#caresearch_accordion"><i aria-hidden="true" class="fal fa-chevron-down"></i></button>
<ul class="collapse" id="caresearch_accordion">
<li>
<a class="active" href="/">Care Homes</a>
</li>
<li class="panel">
<a class="dropdown-toggle collapsed " data-parent="#caresearch_accordion" data-toggle="collapse" href="#othercaresettings">Other Care Settings</a>
<ul class="collapse" id="othercaresettings">
<li>
<a href="/extra-care-housing/" title="Extra Care Housing">Extra Care Housing</a>
</li>
<li>
<a href="/day-care-centres/" title="Adult Day Care Centres">Adult Day Care Centres</a>
</li>
<li>
<a href="/mental-health-hospitals/" title="Mental Health Hospitals">Mental Health Hospitals</a>
</li>
</ul>
</li>
<li>
<a href="/caregroups/">Groups</a>
</li>
<li>
<a href="/awards">Awards</a>
</li>
<li>
<a href="/submitreview">Submit a Review</a>
</li>
</ul>
</li>, <li>
<a class="active" href="/">Care Homes</a>
</li>, <li class="panel">
<a class="dropdown-toggle collapsed " data-parent="#caresearch_accordion" data-toggle="collapse" href="#othercaresettings">Other Care Settings</a>
<ul class="collapse" id="othercaresettings">
<li>
<a href="/extra-care-housing/" title="Extra Care Housing">Extra Care Housing</a>
</li>
<li>
<a href="/day-care-centres/" title="Adult Day Care Centres">Adult Day Care Centres</a>
</li>
<li>
<a href="/mental-health-hospitals/" title="Mental Health Hospitals">Mental Health Hospitals</a>
</li>
</ul>
</li>, <li>
<a href="/extra-care-housing/" title="Extra Care Housing">Extra Care Housing</a>
</li>, <li>
<a href="/day-care-centres/" title="Adult Day Care Centres">Adult Day Care Centres</a>
</li>, <li>
<a href="/mental-health-hospitals/" title="Mental Health Hospitals">Mental Health Hospitals</a>
</li>, <li>
<a href="/caregroups/">Groups</a>
</li>, <li>
<a href="/awards">Awards</a>
</li>, <li>
<a href="/submitreview">Submit a Review</a>
</li>, <li class="panel">
<a class="w-100" href="/advice"><span style="border:none">Care Advice</span></a>
</li>, <li class="panel">
<a href="/jobs/"><span>Job Search</span></a> <button data-parent="#accordion" data-toggle="collapse" href="#jobsearch"><i aria-hidden="true" class="fal fa-chevron-down"></i></button>
<ul class="collapse" id="jobsearch">
<li><a class="active" href="/jobs/">Jobs</a></li>
<li><a class="" href="/account/mycv">Register CV</a></li>
</ul>
</li>, <li><a class="active" href="/jobs/">Jobs</a></li>, <li><a class="" href="/account/mycv">Register CV</a></li>, <li class="panel">
<a data-parent="#accordion" data-toggle="collapse" href="#Industry_accordion"><span>Industry Resources</span></a> <button data-parent="#accordion" data-toggle="collapse" href="#Industry_accordion"><i aria-hidden="true" class="fal fa-chevron-down"></i></button>
<ul class="collapse" id="Industry_accordion">
<li class=""><a class="" href="/suppliers_search.cfm/">Products &amp; Services</a></li>
<li class="panel">
<a class="dropdown-toggle collapsed " data-parent="#Industry_accordion" data-toggle="collapse" href="#Forsale_accordion"> Care Homes For Sale</a>
<ul class="collapse active " id="Forsale_accordion">
<li><a class="" href="/for-sale/">Care Homes For Sale</a></li>
<li><a class="" href="/for-sale/sold.cfm">Care Homes Sold</a></li>
<li><a class="" href="/for-sale/buying_and_selling.cfm">Advice on Buying or Selling a Care Home</a></li>
</ul>
</li>
<li class=""><a class="" href="/care-training/">Training Courses</a></li>
<li class="panel">
<a class="dropdown-toggle collapsed " data-parent="#Industry_accordion" data-toggle="collapse" href="#News_accordion"> News &amp; Events</a>
<ul class="collapse" id="News_accordion">
<li><a class="" href="/news/">News</a></li>
<li><a class="" href="/podcast">Podcast</a> </li>
<li><a class="" href="/news/events.cfm">Events</a></li>
<li><a class="" href="/news/press">Press Room</a></li>
</ul>
</li>
<li class="panel">
<a class="dropdown-toggle collapsed" data-parent="#services" data-toggle="collapse" href="#For_care_homes">Promote your Care Home</a>
<ul class="collapse" id="For_care_homes">
<li>
<a class=" " href="/ourservices">Overview</a></li>
<li><a class=" " href="/ourservices/compare">Enhanced / Premium / Platinum</a>
</li>
<li class="panel">
<a class="dropdown-toggle collapsed" data-parent="#For_care_homes" data-toggle="collapse" href="#Features_accordion"> Features</a>
<ul class="collapse" id="Features_accordion">
<li><a href="/advertise.cfm/page/features">Area Features</a></li>
<li><a href="/advertise.cfm/page/categoryfeatures">Category Features</a></li>
<li><a href="/advertise.cfm/page/competitorfeatures">Competitor Features</a></li>
<li><a href="advertise.cfm/page/groupcompetitorfeatures">Group Competitor Features</a></li>
<li><a href="/advertise.cfm/page/featured-groups">Group Features</a></li>
</ul>
</li>
<li><a class=" " href="/advertise.cfm/page/newsletter">Newsletter</a></li>
<li><a class=" " href="/jobs/post_a_care_job.cfm">Post Jobs</a></li>
<li><a class=" " href="/cv/">CV Search</a></li>
</ul>
</li>
<li class="panel">
<a class="dropdown-toggle collapsed" data-parent="#services" data-toggle="collapse" href="#For_Suppliers">Promote your Products/Services to Care Homes</a>
<ul class="collapse" id="For_Suppliers">
<li><a class=" " href="/ourservices/suppliers">Overview</a></li>
<li><a class=" " href="/advertise_supplier.cfm/page/webadvertisesupplier">Sponsored Service</a></li>
<li><a class=" " href="/advertise_supplier.cfm/page/featured_listings">Features</a></li>
<li><a class=" " href="/advertise_supplier.cfm/page/newsletter">Newsletter</a></li>
<li><a class=" " href="/jobs/post_a_care_job.cfm/page/suppliers">Post Jobs</a></li>
<li><a class="" href="/cv/suppliers">CV Search</a></li>
<li><a class="" href="/for-sale/post_a_property.cfm">For Sale</a></li>
<li><a class="" href="/care-training/post_a_training_course.cfm">Training</a></li>
<li><a class="" href="/disk.cfm">Data</a></li>
<li><a class="" href="/advertise_supplier.cfm/page/supplierentry">New Entry</a></li>
<li><a class="" href="/advertise_supplier.cfm/page/supplieroverview">Web Stats</a></li>
</ul>
</li>
</ul>
</li>, <li class=""><a class="" href="/suppliers_search.cfm/">Products &amp; Services</a></li>, <li class="panel">
<a class="dropdown-toggle collapsed " data-parent="#Industry_accordion" data-toggle="collapse" href="#Forsale_accordion"> Care Homes For Sale</a>
<ul class="collapse active " id="Forsale_accordion">
<li><a class="" href="/for-sale/">Care Homes For Sale</a></li>
<li><a class="" href="/for-sale/sold.cfm">Care Homes Sold</a></li>
<li><a class="" href="/for-sale/buying_and_selling.cfm">Advice on Buying or Selling a Care Home</a></li>
</ul>
</li>, <li><a class="" href="/for-sale/">Care Homes For Sale</a></li>, <li><a class="" href="/for-sale/sold.cfm">Care Homes Sold</a></li>, <li><a class="" href="/for-sale/buying_and_selling.cfm">Advice on Buying or Selling a Care Home</a></li>, <li class=""><a class="" href="/care-training/">Training Courses</a></li>, <li class="panel">
<a class="dropdown-toggle collapsed " data-parent="#Industry_accordion" data-toggle="collapse" href="#News_accordion"> News &amp; Events</a>
<ul class="collapse" id="News_accordion">
<li><a class="" href="/news/">News</a></li>
<li><a class="" href="/podcast">Podcast</a> </li>
<li><a class="" href="/news/events.cfm">Events</a></li>
<li><a class="" href="/news/press">Press Room</a></li>
</ul>
</li>, <li><a class="" href="/news/">News</a></li>, <li><a class="" href="/podcast">Podcast</a> </li>, <li><a class="" href="/news/events.cfm">Events</a></li>, <li><a class="" href="/news/press">Press Room</a></li>, <li class="panel">
<a class="dropdown-toggle collapsed" data-parent="#services" data-toggle="collapse" href="#For_care_homes">Promote your Care Home</a>
<ul class="collapse" id="For_care_homes">
<li>
<a class=" " href="/ourservices">Overview</a></li>
<li><a class=" " href="/ourservices/compare">Enhanced / Premium / Platinum</a>
</li>
<li class="panel">
<a class="dropdown-toggle collapsed" data-parent="#For_care_homes" data-toggle="collapse" href="#Features_accordion"> Features</a>
<ul class="collapse" id="Features_accordion">
<li><a href="/advertise.cfm/page/features">Area Features</a></li>
<li><a href="/advertise.cfm/page/categoryfeatures">Category Features</a></li>
<li><a href="/advertise.cfm/page/competitorfeatures">Competitor Features</a></li>
<li><a href="advertise.cfm/page/groupcompetitorfeatures">Group Competitor Features</a></li>
<li><a href="/advertise.cfm/page/featured-groups">Group Features</a></li>
</ul>
</li>
<li><a class=" " href="/advertise.cfm/page/newsletter">Newsletter</a></li>
<li><a class=" " href="/jobs/post_a_care_job.cfm">Post Jobs</a></li>
<li><a class=" " href="/cv/">CV Search</a></li>
</ul>
</li>, <li>
<a class=" " href="/ourservices">Overview</a></li>, <li><a class=" " href="/ourservices/compare">Enhanced / Premium / Platinum</a>
</li>, <li class="panel">
<a class="dropdown-toggle collapsed" data-parent="#For_care_homes" data-toggle="collapse" href="#Features_accordion"> Features</a>
<ul class="collapse" id="Features_accordion">
<li><a href="/advertise.cfm/page/features">Area Features</a></li>
<li><a href="/advertise.cfm/page/categoryfeatures">Category Features</a></li>
<li><a href="/advertise.cfm/page/competitorfeatures">Competitor Features</a></li>
<li><a href="advertise.cfm/page/groupcompetitorfeatures">Group Competitor Features</a></li>
<li><a href="/advertise.cfm/page/featured-groups">Group Features</a></li>
</ul>
</li>, <li><a href="/advertise.cfm/page/features">Area Features</a></li>, <li><a href="/advertise.cfm/page/categoryfeatures">Category Features</a></li>, <li><a href="/advertise.cfm/page/competitorfeatures">Competitor Features</a></li>, <li><a href="advertise.cfm/page/groupcompetitorfeatures">Group Competitor Features</a></li>, <li><a href="/advertise.cfm/page/featured-groups">Group Features</a></li>, <li><a class=" " href="/advertise.cfm/page/newsletter">Newsletter</a></li>, <li><a class=" " href="/jobs/post_a_care_job.cfm">Post Jobs</a></li>, <li><a class=" " href="/cv/">CV Search</a></li>, <li class="panel">
<a class="dropdown-toggle collapsed" data-parent="#services" data-toggle="collapse" href="#For_Suppliers">Promote your Products/Services to Care Homes</a>
<ul class="collapse" id="For_Suppliers">
<li><a class=" " href="/ourservices/suppliers">Overview</a></li>
<li><a class=" " href="/advertise_supplier.cfm/page/webadvertisesupplier">Sponsored Service</a></li>
<li><a class=" " href="/advertise_supplier.cfm/page/featured_listings">Features</a></li>
<li><a class=" " href="/advertise_supplier.cfm/page/newsletter">Newsletter</a></li>
<li><a class=" " href="/jobs/post_a_care_job.cfm/page/suppliers">Post Jobs</a></li>
<li><a class="" href="/cv/suppliers">CV Search</a></li>
<li><a class="" href="/for-sale/post_a_property.cfm">For Sale</a></li>
<li><a class="" href="/care-training/post_a_training_course.cfm">Training</a></li>
<li><a class="" href="/disk.cfm">Data</a></li>
<li><a class="" href="/advertise_supplier.cfm/page/supplierentry">New Entry</a></li>
<li><a class="" href="/advertise_supplier.cfm/page/supplieroverview">Web Stats</a></li>
</ul>
</li>, <li><a class=" " href="/ourservices/suppliers">Overview</a></li>, <li><a class=" " href="/advertise_supplier.cfm/page/webadvertisesupplier">Sponsored Service</a></li>, <li><a class=" " href="/advertise_supplier.cfm/page/featured_listings">Features</a></li>, <li><a class=" " href="/advertise_supplier.cfm/page/newsletter">Newsletter</a></li>, <li><a class=" " href="/jobs/post_a_care_job.cfm/page/suppliers">Post Jobs</a></li>, <li><a class="" href="/cv/suppliers">CV Search</a></li>, <li><a class="" href="/for-sale/post_a_property.cfm">For Sale</a></li>, <li><a class="" href="/care-training/post_a_training_course.cfm">Training</a></li>, <li><a class="" href="/disk.cfm">Data</a></li>, <li><a class="" href="/advertise_supplier.cfm/page/supplierentry">New Entry</a></li>, <li><a class="" href="/advertise_supplier.cfm/page/supplieroverview">Web Stats</a></li>, <li class="d-none d-sm-block nav-item active">
<a class="nav-link waves-effect waves-light" href="/">Care Search</a>
</li>, <li class="d-block d-sm-none nav-item dropdown active">
<button aria-expanded="false" aria-haspopup="true" class="nav-link dropdown-toggle" data-toggle="dropdown" id="careseach-nav" type="button">
                                                Care Search
                                        </button>
<div aria-labelledby="careseach-subnav" class="dropdown-menu" id="careseach-subnav">
</div>
</li>, <li class="nav-item ">
<a class="nav-link waves-effect waves-light" href="/advice/">Care Advice</a>
</li>, <li class="nav-item ">
<a class="nav-link waves-effect waves-light" href="/jobs/">Job Search</a>
</li>, <li class="nav-item dropdown ">
<button aria-expanded="false" aria-haspopup="true" class="nav-link dropdown-toggle" data-toggle="dropdown" id="IndustryResources-nav" type="button">
                                                Industry Resources
                                        </button>
<div aria-labelledby="IndustryResources-nav" class="dropdown-menu">
<a class="dropdown-item waves-effect waves-light" href="/suppliers_search.cfm/">Products &amp; Services</a>
<a class="dropdown-item waves-effect waves-light" href="/for-sale/">Care Homes For Sale</a>
<a class="dropdown-item waves-effect waves-light" href="/care-training/">Training Courses</a>
<a class="dropdown-item waves-effect waves-light" href="/news/">News &amp; Events</a>
<a class="dropdown-item waves-effect waves-light" href="/ourservices">Promote your Care Home</a>
<a class="dropdown-item waves-effect waves-light" href="/ourservices/suppliers">Promote your Products/Services to Care Homes</a>
</div>
</li>, <li class="nav-item dropdown ">
<button aria-expanded="false" aria-haspopup="true" class="nav-link dropdown-toggle" data-toggle="dropdown" id="user-nav" type="button">

                                                        My
                                                carehome.co.uk
                                        </button>
<div aria-labelledby="user-nav" class="dropdown-menu">
<a class="dropdown-item waves-effect waves-light" onclick="location.href='/signup';">Sign Up</a>
<a class="dropdown-item waves-effect waves-light" onclick="location.href='/login';">Log In</a>
<a class="dropdown-item waves-effect waves-light" href="/account">My Account</a>
<strong>All Users</strong>
<a class="dropdown-item waves-effect waves-light" href="/my_folder.cfm">Folder</a>
<a class="dropdown-item waves-effect waves-light" href="/my_saved_folders.cfm">Saved Folders</a>
<a class="dropdown-item waves-effect waves-light" href="/compare.cfm">Compare</a>
<a class="dropdown-item waves-effect waves-light" href="/recently_viewed.cfm">Recently Viewed</a>
<strong>Jobseekers</strong>
<a class="dropdown-item waves-effect waves-light" href="/account/mycv">Register CV</a>
<a class="dropdown-item waves-effect waves-light" href="/my_jobs_folder.cfm">Job Folders</a>
<a class="dropdown-item waves-effect waves-light" href="/my_saved_jobs.cfm">Saved Job Folder</a>
<a class="dropdown-item waves-effect waves-light" href="/my_jobs.cfm">Job Applications</a>
<a class="dropdown-item waves-effect waves-light" href="/my_job_alerts.cfm">Saved Job Searches / Alerts</a>
</div>
</li>, <li class="nav-item ">
<button class="btn btn-outline-primary m-0 ml-1 waves-effect waves-light" onclick="location.href='/login';">Log In</button>
</li>, <li class="nav-item active">
<a class="nav-link waves-effect waves-light" href="/">Care Homes</a></li>, <li class="nav-item dropdown ">
<button aria-expanded="false" aria-haspopup="true" class="nav-link dropdown-toggle" data-toggle="dropdown" type="button">Other Care Settings</button>
<ul aria-labelledby="CareSettings-nav" class="dropdown-menu">
<li class="nav-item"><a class="nav-link waves-effect waves-light" href="/extra-care-housing/" title="Extra Care Housing">Extra Care Housing</a></li>
<li class="nav-item"><a class="nav-link waves-effect waves-light" href="/day-care-centres/" title="Adult Day Care Centres">Adult Day Care Centres</a></li>
<li class="nav-item"><a class="nav-link waves-effect waves-light" href="/mental-health-hospitals/" title="Mental Health Hospitals">Mental Health Hospitals</a></li>
</ul>
</li>, <li class="nav-item"><a class="nav-link waves-effect waves-light" href="/extra-care-housing/" title="Extra Care Housing">Extra Care Housing</a></li>, <li class="nav-item"><a class="nav-link waves-effect waves-light" href="/day-care-centres/" title="Adult Day Care Centres">Adult Day Care Centres</a></li>, <li class="nav-item"><a class="nav-link waves-effect waves-light" href="/mental-health-hospitals/" title="Mental Health Hospitals">Mental Health Hospitals</a></li>, <li class="nav-item d-none d-sm-block "><a class="nav-link waves-effect waves-light" href="/caregroups/">Groups</a></li>, <li class="nav-item dropdown d-block d-sm-none">
<button aria-expanded="false" aria-haspopup="true" class="nav-link dropdown-toggle" data-toggle="dropdown" type="button">Groups</button>
<ul class="dropdown-menu">
<li class="nav-item"><a class="nav-link waves-effect waves-light" href="/caregroups/">Groups with Enhanced / Premium /<br>Platinum Services</br></a></li>
<li class="nav-item"><a class="nav-link waves-effect waves-light" href="/caregroups/allcarehomegroups.cfm">All Groups</a></li>
</ul>
</li>, <li class="nav-item"><a class="nav-link waves-effect waves-light" href="/caregroups/">Groups with Enhanced / Premium /<br>Platinum Services</br></a></li>, <li class="nav-item"><a class="nav-link waves-effect waves-light" href="/caregroups/allcarehomegroups.cfm">All Groups</a></li>, <li class="nav-item "><a class="nav-link waves-effect waves-light" href="/awards">Awards</a></li>, <li class="nav-item"><a class="nav-link waves-effect waves-light" href="/submitreview">Submit a Review</a></li>, <li class="breadcrumb-item small d-none d-sm-inline-block"><a href="https://www.carehome.co.uk">UK Care Homes Search</a></li>, <li class="breadcrumb-item small d-none d-sm-inline-block"><a href="https://www.carehome.co.uk/care_search_results.cfm/searchcountry/England">Care Homes in England</a></li>, <li class="breadcrumb-item small d-none d-sm-inline-block"><a href="https://www.carehome.co.uk/care_search_results.cfm/searchregion/South-East-England">Care Homes in South East England</a></li>, <li class="breadcrumb-item small d-none d-sm-inline-block"><a href="https://www.carehome.co.uk/care_search_results.cfm/searchcounty/Surrey">Care Homes in Surrey</a></li>, <li class="breadcrumb-item small d-none d-sm-inline-block"><a href="https://www.carehome.co.uk/care_search_results.cfm/searchunitary/Woking">Care Homes Woking Area</a></li>, <li class="breadcrumb-item mobile_breadcrumb small"><a href="https://www.carehome.co.uk/care_search_results.cfm/searchtown/West-Byfleet"><span class="d-inline d-sm-none">View </span>Care Homes in West Byfleet</a></li>, <li class="breadcrumb-item small d-none d-sm-inline-block">West Hall care home
                                </li>, <li class="breadcrumb-item mobile_breadcrumb small"><a href="https://www.carehome.co.uk/care_search_results.cfm/searchtown/West-Byfleet"><span class="d-inline d-sm-none">View </span>Care Homes in West Byfleet</a></li>, <li class="nav-item">
<button class="btn btn-danger open_accordion booktour btn booktourbutton btn-danger waves-effect waves-light" data-ga-category="Profile Button" data-ga-event-tracking="1" data-ga-label="Tour" data-ga-track-click="1" data-id="booktour" data-target="#bookatourModal" data-toggle="modal" id="bookatour">
<i aria-hidden="true" class="fad fa-calendar-alt d-block d-sm-none"></i>  Book a Tour
                        </button>
</li>, <li class="nav-item">
<a class="btn btn-primary nav-link waves-effect waves-light" data-ga-category="Profile Button" data-ga-event-tracking="1" data-ga-label="Website" data-ga-track-click="1" href="https://www.carehome.co.uk/externalsite.cfm?searchazref=83165&amp;linkcategory=carehome" id="website-button" target="_blank"><i aria-hidden="true" class="fad fa-browser d-block d-sm-none"></i> <span class="d-none d-sm-inline">Visit </span>Website</a>
</li>, <li class="nav-item">
<button class="btn btn-primary nav-link ajax waves-effect waves-light" data-ga-category="Profile Button" data-ga-event-tracking="1" data-ga-label="Email" data-ga-track-click="1" data-target="#ajaxModal" data-toggle="modal" href="https://www.carehome.co.uk/window-content/enquiry_brochure_request.cfm?uniqueid=83165&amp;contact_type=email" id="brochure_email"><i aria-hidden="true" class="fad fa-envelope d-block d-sm-none"></i> <span class="d-none d-sm-inline">Send </span>Email</button>
</li>, <li class="nav-item">
<button class="btn btn-primary nav-link ajax waves-effect waves-light" data-ga-category="Profile Button" data-ga-event-tracking="1" data-ga-label="Phone" data-ga-track-click="1" data-target="#ajaxModal" data-toggle="modal" href="https://www.carehome.co.uk/window-content/enquiry_brochure_request.cfm?uniqueid=83165&amp;contact_type=phone" id="brochure_phone"><i aria-hidden="true" class="fad fa-phone d-block d-sm-none"></i> <span class="d-none d-sm-inline">View Phone Number</span><span class="d-block d-sm-none">Call</span></button>
</li>, <li class="nav-item">
<button class="btn btn-primary nav-link ajax waves-effect waves-light" data-ga-category="Profile Button" data-ga-event-tracking="1" data-ga-label="Brochure" data-ga-track-click="1" data-target="#ajaxModal" data-toggle="modal" href="https://www.carehome.co.uk/window-content/enquiry_brochure_request.cfm?uniqueid=83165&amp;contact_type=brochure" id="brochure_brochure"><i aria-hidden="true" class="fad fa-book d-block d-sm-none"></i> <span class="d-none d-sm-inline">Request a </span>Brochure</button>
</li>, <li class="nav-item ml-sm-auto">
<a class="btn btn-success btn-jobs nav-link waves-effect waves-light" data-ga-category="Profile Button" data-ga-event-tracking="1" data-ga-label="Jobs" data-ga-track-click="1" href="https://www.carehome.co.uk/jobs/index.cfm/agent_id/83165?ref=profile"><i aria-hidden="true" class="fad fa-users d-block d-sm-none"></i> Jobs</a>
</li>, <li class="nav-item p-0">
<a class="nav-link active" data-target="#general-info" href="https://www.carehome.co.uk/carehome.cfm/searchazref/83165#top">Overview</a>
</li>, <li class="nav-item">
<a class="nav-link" data-target="#reviews" href="https://www.carehome.co.uk/carehome.cfm/searchazref/83165#reviews">Reviews (98)</a>
</li>, <li class="nav-item">
<button class="nav-link ajax" data-target="#ajaxModal" data-toggle="modal" href="https://www.carehome.co.uk/member/profile/gallery/uniqueid/83165" rel="nofollow" type="button">
<span class="d-inline d-sm-none">Gallery</span><span class="d-none d-sm-inline">Photos (13) / Video (2) / '360' Tour (1)</span>
</button>
</li>, <li class="nav-item">
<a class="nav-link" data-target="#performance" href="https://www.carehome.co.uk/carehome.cfm/searchazref/83165#performance">Performance</a>
</li>, <li class="nav-item">
<a class="nav-link " data-target="#bed-vacancies" href="https://www.carehome.co.uk/carehome.cfm/searchazref/83165#bed-vacancies">Bed Vacancies</a>
</li>, <li class="nav-item">
<a class="nav-link" data-target="#awards-ratings" href="https://www.carehome.co.uk/carehome.cfm/searchazref/83165#awards-ratings">Awards (6)</a>
</li>, <li class="nav-item">
<a class="nav-link" data-target="#news-articles" href="https://www.carehome.co.uk/carehome.cfm/searchazref/83165#news-articles">News (36)  &amp; Events (0)</a>
</li>, <li class="nav-item">
<a class="nav-link" data-target="#staff-profiles" href="https://www.carehome.co.uk/carehome.cfm/searchazref/83165#staff-profiles">Team (0)</a>
</li>, <li><div class="h4">Type of Service</div></li>, <li>
                    Care Home only (Residential Care)
                        – Voluntary / Not for Profit Owned

                </li>, <li>
                        Registered for a maximum of 117 Service Users
                    </li>, <li><div class="h4">Registered Care Categories*</div></li>, <li>
                            Dementia
                        </li>, <li>
                            Old Age
                        </li>, <li>
                            Physical Disability
                        </li>, <li>
                            Sensory Impairment
                        </li>, <li><small>*Registered with regulator 'Care Quality Commission (CQC)' to provide these categories of care</small></li>, <li><div class="h4">Specialist Care Categories</div></li>, <li>
                            Alzheimer's
                        </li>, <li><div class="h4">Other Care Provided</div></li>, <li>Convalescent Care</li>, <li>Own GP if required</li>, <li>Respite Care</li>, <li><div class="h4">Group/Owner</div></li>, <li>
<a href="https://www.carehome.co.uk/care_search_results.cfm/searchgroup/36154006ANCA">Anchor</a>
</li>, <li><div class="h4">Person in charge</div></li>, <li>Katherine Mahoney (Manager)</li>, <li><div class="h4">Local Authority / Social Services</div></li>, <li>Surrey County Council (<a href="https://www.carehome.co.uk/local-authorities/profile.cfm/id/Surrey">click for contact details</a>)</li>, <li><div class="h4">Admission Information</div></li>, <li>
                    Ages 65+.
                </li>, <li><div class="h4">Room Information</div></li>, <li>Single Rooms 117</li>, <li>Rooms with ensuite WC 117</li>, <li>Bar/Cafe on premises</li>, <li>Gardens for residents</li>, <li>Lift</li>, <li>Minibus or other transport</li>, <li>Pets by arrangement</li>, <li>Phone Point in own room/Mobile</li>, <li>Television point in own room</li>, <li>Wheelchair access</li>, <li class="checkbox">
<input class="filter-review filter-review-sync" id="filter_review_rating_5" name="filter_review_rating_5" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Avg Rating - Excellent'})" type="checkbox" value="5">
<label for="filter_review_rating_5">
<span>Excellent</span>
</label>
<span class="review_bar">
<span class="review_fill" style="width:86.7346938776%"></span>
</span>
<div class="review_bar_label_r">85</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review-sync" id="filter_review_rating_4" name="filter_review_rating_4" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Avg Rating - Good'})" type="checkbox" value="4">
<label for="filter_review_rating_4">
<span>Good</span>
</label>
<span class="review_bar">
<span class="review_fill" style="width:13.2653061224%"></span>
</span>
<div class="review_bar_label_r">13</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review-sync" id="filter_review_rating_3" name="filter_review_rating_3" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Avg Rating - Satisfactory'})" type="checkbox" value="3">
<label for="filter_review_rating_3">
<span>Satisfactory</span>
</label>
<span class="review_bar">
<span class="review_fill" style="width:0%"></span>
</span>
<div class="review_bar_label_r">0</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review-sync" id="filter_review_rating_2" name="filter_review_rating_2" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Avg Rating - Poor'})" type="checkbox" value="2">
<label for="filter_review_rating_2">
<span>Poor</span>
</label>
<span class="review_bar">
<span class="review_fill" style="width:0%"></span>
</span>
<div class="review_bar_label_r">0</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review-sync" id="filter_review_rating_1" name="filter_review_rating_1" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Avg Rating - Very Poor'})" type="checkbox" value="1">
<label for="filter_review_rating_1">
<span>Very Poor</span>
</label>
<span class="review_bar">
<span class="review_fill" style="width:0%"></span>
</span>
<div class="review_bar_label_r">0</div>
</input></li>, <li class="checkbox">
<input class="filter-review" id="filter_review_likely_5" name="filter_review_likely_5" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'How Likely - Extremely LIKELY'})" type="checkbox" value="5">
<label for="filter_review_likely_5">
<span>Extremely LIKELY</span>
</label>
<span class="review_bar">
<span class="review_fill" style="width:88.7755102041%"></span>
</span>
<div class="review_bar_label_r">87</div>
</input></li>, <li class="checkbox">
<input class="filter-review" id="filter_review_likely_4" name="filter_review_likely_4" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'How Likely - Likely'})" type="checkbox" value="4">
<label for="filter_review_likely_4">
<span>Likely</span>
</label>
<span class="review_bar">
<span class="review_fill" style="width:11.2244897959%"></span>
</span>
<div class="review_bar_label_r">11</div>
</input></li>, <li class="checkbox">
<input class="filter-review" id="filter_review_likely_3" name="filter_review_likely_3" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'How Likely - Don't know'})" type="checkbox" value="3">
<label for="filter_review_likely_3">
<span>Don't know</span>
</label>
<span class="review_bar">
<span class="review_fill" style="width:0%"></span>
</span>
<div class="review_bar_label_r">0</div>
</input></li>, <li class="checkbox">
<input class="filter-review" id="filter_review_likely_2" name="filter_review_likely_2" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'How Likely - Neither Unlikely or Likely'})" type="checkbox" value="2">
<label for="filter_review_likely_2">
<span>Neither Unlikely or Likely</span>
</label>
<span class="review_bar">
<span class="review_fill" style="width:0%"></span>
</span>
<div class="review_bar_label_r">0</div>
</input></li>, <li class="checkbox">
<input class="filter-review" id="filter_review_likely_1" name="filter_review_likely_1" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'How Likely - Unlikely'})" type="checkbox" value="1">
<label for="filter_review_likely_1">
<span>Unlikely</span>
</label>
<span class="review_bar">
<span class="review_fill" style="width:0%"></span>
</span>
<div class="review_bar_label_r">0</div>
</input></li>, <li class="checkbox">
<input class="filter-review" id="filter_review_likely_0" name="filter_review_likely_0" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'How Likely - Extremely UNLIKELY'})" type="checkbox" value="0">
<label for="filter_review_likely_0">
<span>Extremely UNLIKELY</span>
</label>
<span class="review_bar">
<span class="review_fill" style="width:0%"></span>
</span>
<div class="review_bar_label_r">0</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review_connection" id="filter_review_connection_9" name="filter_review_connection_9" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Connection - Daughter of Resident/Service User'})" type="checkbox" value="9">
<label for="filter_review_connection_9">
<span>Daughter of Resident/Service User</span>
</label>
<div class="review_bar_label_r">39</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review_connection" id="filter_review_connection_8" name="filter_review_connection_8" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Connection - Son of Resident/Service User'})" type="checkbox" value="8">
<label for="filter_review_connection_8">
<span>Son of Resident/Service User</span>
</label>
<div class="review_bar_label_r">17</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review_connection" id="filter_review_connection_5" name="filter_review_connection_5" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Connection - Wife of Resident/Service User'})" type="checkbox" value="5">
<label for="filter_review_connection_5">
<span>Wife of Resident/Service User</span>
</label>
<div class="review_bar_label_r">11</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review_connection" id="filter_review_connection_1" name="filter_review_connection_1" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Connection - Resident / Service User'})" type="checkbox" value="1">
<label for="filter_review_connection_1">
<span>Resident / Service User</span>
</label>
<div class="review_bar_label_r">7</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review_connection" id="filter_review_connection_23" name="filter_review_connection_23" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Connection - Friend of Resident/Service User'})" type="checkbox" value="23">
<label for="filter_review_connection_23">
<span>Friend of Resident/Service User</span>
</label>
<div class="review_bar_label_r">6</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review_connection" id="filter_review_connection_90" name="filter_review_connection_90" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Connection - Daughter-in-law of Resident/Service User'})" type="checkbox" value="90">
<label for="filter_review_connection_90">
<span>Daughter-in-law of Resident/Service User</span>
</label>
<div class="review_bar_label_r">4</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review_connection" id="filter_review_connection_171" name="filter_review_connection_171" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Connection - Respite Resident/Service User'})" type="checkbox" value="171">
<label for="filter_review_connection_171">
<span>Respite Resident/Service User</span>
</label>
<div class="review_bar_label_r">3</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review_connection" id="filter_review_connection_6" name="filter_review_connection_6" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Connection - Husband of Resident/Service User'})" type="checkbox" value="6">
<label for="filter_review_connection_6">
<span>Husband of Resident/Service User</span>
</label>
<div class="review_bar_label_r">2</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review_connection" id="filter_review_connection_14" name="filter_review_connection_14" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Connection - Nephew of Resident/Service User'})" type="checkbox" value="14">
<label for="filter_review_connection_14">
<span>Nephew of Resident/Service User</span>
</label>
<div class="review_bar_label_r">2</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review_connection" id="filter_review_connection_22" name="filter_review_connection_22" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Connection - Relative of Resident/Service User'})" type="checkbox" value="22">
<label for="filter_review_connection_22">
<span>Relative of Resident/Service User</span>
</label>
<div class="review_bar_label_r">2</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review_connection" id="filter_review_connection_7" name="filter_review_connection_7" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Connection - Cousin of Resident/Service User'})" type="checkbox" value="7">
<label for="filter_review_connection_7">
<span>Cousin of Resident/Service User</span>
</label>
<div class="review_bar_label_r">1</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review_connection" id="filter_review_connection_15" name="filter_review_connection_15" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Connection - Niece of Resident/Service User'})" type="checkbox" value="15">
<label for="filter_review_connection_15">
<span>Niece of Resident/Service User</span>
</label>
<div class="review_bar_label_r">1</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review_connection" id="filter_review_connection_2" name="filter_review_connection_2" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Connection - Power of Attorney of Resident/Service User'})" type="checkbox" value="2">
<label for="filter_review_connection_2">
<span>Power of Attorney of Resident/Service User</span>
</label>
<div class="review_bar_label_r">1</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review_connection" id="filter_review_connection_4" name="filter_review_connection_4" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Connection - Sister of Resident/Service User'})" type="checkbox" value="4">
<label for="filter_review_connection_4">
<span>Sister of Resident/Service User</span>
</label>
<div class="review_bar_label_r">1</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review_connection" id="filter_review_connection_88" name="filter_review_connection_88" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Connection - Son-in-law of Resident/Service User'})" type="checkbox" value="88">
<label for="filter_review_connection_88">
<span>Son-in-law of Resident/Service User</span>
</label>
<div class="review_bar_label_r">1</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review-sync" id="filter_review_rating_5" name="filter_review_rating_5" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Avg Rating - Excellent'})" type="checkbox" value="5">
<label for="filter_review_rating_5">
<span>Excellent</span>
</label>
<span class="review_bar">
<span class="review_fill" style="width:86.7346938776%"></span>
</span>
<div class="review_bar_label_r">85</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review-sync" id="filter_review_rating_4" name="filter_review_rating_4" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Avg Rating - Good'})" type="checkbox" value="4">
<label for="filter_review_rating_4">
<span>Good</span>
</label>
<span class="review_bar">
<span class="review_fill" style="width:13.2653061224%"></span>
</span>
<div class="review_bar_label_r">13</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review-sync" id="filter_review_rating_3" name="filter_review_rating_3" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Avg Rating - Satisfactory'})" type="checkbox" value="3">
<label for="filter_review_rating_3">
<span>Satisfactory</span>
</label>
<span class="review_bar">
<span class="review_fill" style="width:0%"></span>
</span>
<div class="review_bar_label_r">0</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review-sync" id="filter_review_rating_2" name="filter_review_rating_2" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Avg Rating - Poor'})" type="checkbox" value="2">
<label for="filter_review_rating_2">
<span>Poor</span>
</label>
<span class="review_bar">
<span class="review_fill" style="width:0%"></span>
</span>
<div class="review_bar_label_r">0</div>
</input></li>, <li class="checkbox">
<input class="filter-review filter-review-sync" id="filter_review_rating_1" name="filter_review_rating_1" onclick="gtag('event', 'click', { event_category: 'Profile Review Filters', event_action: 'click', event_label: 'Avg Rating - Very Poor'})" type="checkbox" value="1">
<label for="filter_review_rating_1">
<span>Very Poor</span>
</label>
<span class="review_bar">
<span class="review_fill" style="width:0%"></span>
</span>
<div class="review_bar_label_r">0</div>
</input></li>, <li class="page-item active"><a class="page-link waves-effect" href="https://www.carehome.co.uk/carehome.cfm/searchazref/83165/#reviews">1</a></li>, <li class="page-item "><a class="page-link waves-effect" href="https://www.carehome.co.uk/carehome.cfm/searchazref/83165/startpage/2#reviews">2</a></li>, <li class="page-item "><a class="page-link waves-effect" href="https://www.carehome.co.uk/carehome.cfm/searchazref/83165/startpage/3#reviews">3</a></li>, <li class="page-item "><a class="page-link waves-effect" href="https://www.carehome.co.uk/carehome.cfm/searchazref/83165/startpage/4#reviews">4</a></li>, <li class="page-item "><a class="page-link waves-effect" href="https://www.carehome.co.uk/carehome.cfm/searchazref/83165/startpage/5#reviews">5</a></li>, <li class="page-item"><a class="page-link waves-effect" href="https://www.carehome.co.uk/carehome.cfm/searchazref/83165/startpage/2#reviews">Next</a></li>, <li><p>a) The Average Rating is 4.8 out of 5 from 42 Reviews in the last 24 months. </p></li>, <li><p>b) The score for the number of positive Reviews is 5 out of 5 from 42 positive Reviews in the last 24 months.</p></li>, <li>
<p>a) 5 Points are available for the Average Rating of all Reviews in the last 24 months. For each review the Care Home / service is rated Excellent, Good, Satisfactory, Poor or Very Poor on a number of areas eg Staff, Management etc. The Care Home receives points for each rating as follows: Excellent = 5. Good = 4. Satisfactory = 3. Poor = 2. Very Poor = 1. These points are added up and then divided by the total number of completed ratings to generate the average rating.</p>
<p>
<b>
                                                The Average Rating of 4.759 for West Hall is calculated as follows:
                                                (

                                                                (385 Excellents x 5)

                                                                        +

                                                                (106 Goods x 4)

                                                                        +

                                                                (7 Satisfactorys x 3)

                                                )
                                                ÷ 498 Ratings = 4.759
                                                </b>
</p>
</li>, <li>
<p>b) 5 Points are available for the number of Positive Reviews in the last 24 months.
                                                A Positive Review is defined as any Review with 'Extremely Likely' or 'Likely' in answer to the question 'How likely are you to recommend this
                                                care provider to friends and family
                                                 if they needed similar care or treatment?'
                                        </p>
<p><b>The 5 Points relating to the number of positive Reviews for West Hall is based on 42 positive Reviews in the last 24 months and is calculated as per below:</b></p>
<p>The 5 points available are broken down as follows:</p>
<ul>
<li><p>i)
                                                                4 points are available for the first 10 Positive Reviews in the last 24 months; 3 points for the first Positive Review, and then 0.125 Points for each of the next four Positive Reviews and then 0.1 Points for the next five Positive Reviews.

                                                                (1st = 3.000, 2nd = 0.125, 3rd = 0.125, 4th = 0.125, 5th = 0.125, 6th = 0.100, 7th = 0.100, 8th = 0.100, 9th = 0.100, 10th = 0.100)

                                                                <b>
                                                                        3
                                                                                                +
                                                                                        0.125
                                                                                                +
                                                                                        0.125
                                                                                                +
                                                                                        0.125
                                                                                                +
                                                                                        0.125
                                                                                                +
                                                                                        0.1
                                                                                                +
                                                                                        0.1
                                                                                                +
                                                                                        0.1
                                                                                                +
                                                                                        0.1
                                                                                                +
                                                                                        0.1
                                                                        = 4
                                                                </b>
</p></li>
<li><p>ii)
                                                                1 point is available for the number of Positive Reviews reaching 20% of the registered maximum number of service users in the last 24 months. If this number is partially reached, then that proportion of 1 point is given. eg a Care Home registered for a maximum of 50 service users has to reach 10 Positive Reviews to receive 1 point, if it has 7 reviews it will receive 0.7 points.

                                                                <b>

                                                                                        20% of the 117 registered maximum number of service users is 23.4, which has been reached with 42 Positive reviews. Points = 1

                                                                </b>
</p></li>
</ul>
</li>, <li><p>i)
                                                                4 points are available for the first 10 Positive Reviews in the last 24 months; 3 points for the first Positive Review, and then 0.125 Points for each of the next four Positive Reviews and then 0.1 Points for the next five Positive Reviews.

                                                                (1st = 3.000, 2nd = 0.125, 3rd = 0.125, 4th = 0.125, 5th = 0.125, 6th = 0.100, 7th = 0.100, 8th = 0.100, 9th = 0.100, 10th = 0.100)

                                                                <b>
                                                                        3
                                                                                                +
                                                                                        0.125
                                                                                                +
                                                                                        0.125
                                                                                                +
                                                                                        0.125
                                                                                                +
                                                                                        0.125
                                                                                                +
                                                                                        0.1
                                                                                                +
                                                                                        0.1
                                                                                                +
                                                                                        0.1
                                                                                                +
                                                                                        0.1
                                                                                                +
                                                                                        0.1
                                                                        = 4
                                                                </b>
</p></li>, <li><p>ii)
                                                                1 point is available for the number of Positive Reviews reaching 20% of the registered maximum number of service users in the last 24 months. If this number is partially reached, then that proportion of 1 point is given. eg a Care Home registered for a maximum of 50 service users has to reach 10 Positive Reviews to receive 1 point, if it has 7 reviews it will receive 0.7 points.

                                                                <b>

                                                                                        20% of the 117 registered maximum number of service users is 23.4, which has been reached with 42 Positive reviews. Points = 1

                                                                </b>
</p></li>, <li><p>When a Review is submitted by someone who has previously submitted a Review, only the latest Review will count towards the Review Score.</p></li>, <li><p>If a Care Home does not have a review in the last 24 months. then it will not have a Review Score.</p></li>, <li><p>
                                We welcome  residents/service users and their family/friends  to submit reviews to carehome.co.uk
                        </p></li>, <li><p>This is not a formal complaint procedure or to be used for allegations of negligence, abuse or criminal activity. If you wish to make a complaint or have a serious allegation of negligence, please refer to the procedures on our <a href="/complaints/">complaints page</a>.</p></li>, <li><p>Before publication, we check that all reviews comply with our <a href="/terms/#reviews" target="_blank">Review Policy</a> and we show all reviews to care providers. It can take up to 30 days for a review to be published or deemed non-compliant.</p></li>, <li>
<p>Caring</p>
<span class="new_report_rating outstanding">

                                                Outstanding

                                        </span>
</li>, <li>
<p>Effective</p>
<span class="new_report_rating good">

                                                Good

                                        </span>
</li>, <li>
<p>Responsive</p>
<span class="new_report_rating outstanding">

                                                Outstanding

                                        </span>
</li>, <li>
<p>Safe</p>
<span class="new_report_rating good">

                                                Good

                                        </span>
</li>, <li>
<p>Well-led</p>
<span class="new_report_rating outstanding">

                                                Outstanding

                                        </span>
</li>, <li><img alt="Star" data-src="/assets/images/cqc/star.png" height="15" loading="lazy" src="/assets/images/cqc/star.png" title="Star" width="17"> <span>Outstanding - the service is performing exceptionally well.</span></img></li>, <li><img alt="Green smartie" data-src="/assets/images/cqc/green.png" height="15" loading="lazy" src="/assets/images/cqc/green.png" title="Green smartie" width="17"> <span>Good - the service is performing well and meeting our expectations.</span></img></li>, <li><img alt="Yellow smartie" data-src="/assets/images/cqc/yellow.png" height="15" loading="lazy" src="/assets/images/cqc/yellow.png" title="Yellow smartie" width="17"> <span>Requires improvement - the service isn't performing as well as it should and we have told the service how it must improve.</span></img></li>, <li><img alt="Red smartie" data-src="/assets/images/cqc/red.png" height="15" loading="lazy" src="/assets/images/cqc/red.png" title="Red smartie" width="17"> <span>Inadequate - the service is performing badly and we've taken enforcement action against the provider of the service.</span></img></li>, <li><img alt="Grey smartie" data-src="/assets/images/cqc/grey.png" height="15" loading="lazy" src="/assets/images/cqc/grey.png" title="Grey smartie" width="17"> <span>No rating/under appeal/rating suspended - there are some services which we can't rate, while some might be under appeal from the provider. Suspended ratings are being reviewed by us and will be published soon.</span></img></li>, <li><img alt="Green Tick" data-src="/assets/images/cqc/green_tick_small.png" height="15" loading="lazy" src="/assets/images/cqc/green_tick_small.png" title="Green Tick" width="17"> <span>There's no need for the service to take further action. If this service has not had a CQC inspection since it registered with us, our judgement may be based on our assessment of declarations and evidence supplied by the service.</span></img></li>, <li><img alt="Grey Cross" data-src="/assets/images/cqc/grey_cross_small.png" height="15" loading="lazy" src="/assets/images/cqc/grey_cross_small.png" title="Grey Cross" width="17"> <span>The service must make improvements.</span></img></li>, <li><img alt="Red Cross" class="red-cross" data-src="/assets/images/cqc/red_cross_small.png" height="15" loading="lazy" src="/assets/images/cqc/red_cross_small.png" title="Red Cross" width="17"> <span>At least one standard in this area was not being met when we inspected the service and we have taken enforcement action.</span></img></li>, <li><h5>Care Search</h5></li>, <li><a href="https://www.carehome.co.uk">Care Homes</a></li>, <li><a href="/extra-care-housing/">Extra Care Housing</a></li>, <li><a href="/day-care-centres/">Adult Day Care Centres</a></li>, <li><a href="/mental-health-hospitals/">Mental Health Hospitals</a></li>, <li><a href="/caregroups/">Groups</a></li>, <li><a href="/awards/">Awards</a></li>, <li><a href="/submitreview">Submit a Review</a></li>, <li>
<h5>Care Advice</h5>
</li>, <li><a href="/advice">Care Advice Overview</a></li>, <li><a href="/advice/fees">Fees Advice</a></li>, <li><a href="/advice/who-pays-what">Who Pays for What</a></li>, <li><h5>Job Search</h5></li>, <li><a href="/jobs/">Jobs</a></li>, <li><a href="/account/mycv">Register CV</a></li>, <li><a href="/jobs/advice">Jobs Advice</a></li>, <li><h5>Industry Resources</h5></li>, <li><a href="/suppliers_search.cfm">Products &amp; Services</a></li>, <li><a href="/for-sale/">Care Home For Sale</a></li>, <li><a href="/care-training/">Training Courses</a></li>, <li><a href="/news/">News &amp; Events</a></li>, <li><h5>My carehome.co.uk</h5></li>, <li><a href="/account">Account</a></li>, <li><a href="/my_folder.cfm">Folder</a></li>, <li><a href="/recently_viewed.cfm">Recently Viewed</a></li>, <li><h5>carehome.co.uk</h5></li>, <li><a href="/contact.cfm">About carehome.co.uk</a></li>, <li><a href="/ourservices">Promote your Care Home</a></li>, <li><a href="/ourservices/suppliers">Promote your Products/Services to Care Homes</a></li>]'''

textRegext = re.compile(r'''
		(<h2 class=\"mb-3\"|\"h4\")?	 	#antes del signo mayor
		>(\"?[a-zA-Z0-9"'-() ]+\"?)< 		#entre los signos mayores
		''', re.VERBOSE | re.DOTALL)

nombre = textRegext.findall(texto_prueba)
		
try:
    print(nombre)
except:
    print("No se encontro nada!")