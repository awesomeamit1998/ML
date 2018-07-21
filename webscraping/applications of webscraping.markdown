
Upwork

Hiring Headquarters

        Blog Editor's Picks Hiring Resources Get Weekly Updates 

What is Web Scraping and How Can You Use It?

    Hiring Headquarters HomeFor ClientsWhat is Web Scraping and How Can You Use It?

Image for What is Web Scraping and How Can You Use It?

This article originally appeared on JetRuby Blog and has been republished with permission. Find out how to syndicate your content with Upwork.
What is web scraping?

To put in a nutshell, web scraping is a process of data extraction from websites. All the job is carried out by a piece of code which is called a “scraper”. First, it sends a “GET” query to a specific website. Then, it parses an HTML document based on the received result. After it’s done, the scraper searches for the data you need within the document, and, finally, converts it into whatever specified format.
The data can be the following:

    product items;
    images;
    videos;
    text;
    contact information, e.g. emails, phone numbers etc.

Recommended Web Scraping Freelancers
$50/hr
Faruque Azam

Faruque Azam

Web Scraping and Developer
$50/hr
Ihor S.

Ihor S.

Web Scraping (Crawling) Expert
$20/hr
Slawomir D.

Slawomir D.

Excel, VBA and Web Scraping Expert
$25/hr
Fatih Kose

Fatih Kose

Digital Image Processing Engineer & Web Scraping Expert
WHAT DO I USE FOR WEB SCRAPING?

    Separate services that work through an API or have a web interface (Embedly, DiffBot etc.)
    Various open source projects implemented in different programming languages (Python: Goose, Scrapy; PHP: Goutte; Ruby: Readability, Morph, etc.).

On top of that, you can always try and make your own web scraping tool. Luckily, there are plenty of libraries available. For example, you can use the Nokogiri library to make a Ruby-based scraper.
Are there any challenges I may want to know?

Yes, there are. After having some extensive web scraping experience, we’ve outlined a list of things that can prevent you from taking full advantage of web scrapers.

    Most of the websites are simply different layout-wise.
    Amateurs or pros, not all web developers follow style guides. As a result, their code often contains various mistakes making it absolutely unreadable for scrapers.
    Many websites are built with HTML5 in which any element can be unique.

Content copy protection, e.g. a multi-level layout, using JavaScript for content rendering, user-agent validations etc.

    Depending on either the season of the year or the subject of the content itself, some websites can change their layouts. Keeping up with these changes requires a lot of time and effort.
    The abundance of ads, floods of comments, too many navigation elements, etc.
    In the web page code, there can be links to the same images of different size, e.g. image preview.
    Since the choice of language on most of the websites is based on your location, the content may not always be displayed in English.
    Websites can have their own encoding that is impossible to send back with a request.

All these factors directly affect the quality of the content leading to its decrease by unacceptable 10% or even 20%. But I’m dying to scrape some websites! What should I do?

Basically, it all boils down to the following options:

    If the number of websites you’re going to scrape the data from is quite small, it’s better to write your own scraper and customize it according to each specific website. The quality of the output content should be 100%.
    If the number of websites to scrape goes beyond “small”, we suggest using a complex approach. In this case, the output content quality should be close to 95%.

awesome job post
HOW DOES THAT LOOK LIKE IN PRACTICE?

First, you would need to create a mechanism to receive HTML code with a GET request. Next, inspect the DOM structure of the website to identify the nodes containing the target data. After that, create a node processor to output the data in a normalized format. The choice of format is usually based on either your client’s requirements or your data processing preferences. For example, we use JSON. And that’s pretty much it – you can create the scraping system.

We’ve called ours “Duck System”. Why? Well, we just thought life’s just too short to come up with fancy names for a piece of code.

 
Image of web scraping flow

 

Now, let’s break it down. The system receives an URL at the input and outputs normalized data at the output. Upon receiving the URL, the system decides which reader should process it. The priority goes to the most high-quality reader with proper customizations. In case there is no such reader, the URL is forwarded to the default reader. Usually, it’s either the most stable scraper or some third-party service.

As you can see, there is another scraper to the right side of the scheme. It comes into play only when the default reader fails to read an incoming URL. For this purpose, the reader’s database is being constantly updated either by the developers or by the system admin.

We also recommend implementing some sort of a feedback support to be able to promptly receive complaints about low-quality content, if any. Using such system enables us to achieve the highest content quality. However, everything has its price. In this case, the downsides are the increased processing time and server resources as well as the fact that the subscription to the third-party service is paid. Also, it’s quite possible that these expenses may exceed what you’ve spend on the server infrastructure and developers’ work.

The main advantage of going for your own solution to scrape a small number of websites is the processing speed (which takes roughly 7 ms for one web page to process). But what about the bandwidth and upload file size-related limitations? We’ve solved this problem by asynchronously downloading media and main content in the background. As a result, files up to 100MB can be downloaded in a blink of an eye, wherein the quality of the output content remains 100%.
Wrap-up

If you are going to develop your own web scraping system, we can gladly share more of our experience. After all, implementing an efficient scraping system is a much more challenging task than it may seem at first. That’s why it’s important to consider all the possible issues and pitfalls from the very beginning.

This story was submitted by JetRuby and does not constitute the views or opinions of Upwork.

Upwork is a freelancing marketplace where businesses of all sizes can find talented professionals across multiple disciplines and categories. If you are a business and are looking to get projects done, consider signing up!
Join Upwork
JetRuby

by JetRuby @jetrubyagency

JetRuby Agency is a multi-faceted web and mobile development company with deep experience in the business and 80+ successfully accomplished projects for clients from all… more
Related Skills

    back-end development
    PHP
    Python

Previous article
Next article
Related articles
How to Choose a Technology Stack for Web Application Development
August 17, 2017

The right technology stack is, to a great extent, the key to your project’s success. We’ve decided to give you a helping hand and reveal the criteria for choosing the most appropriate tech stack for your web application.
Read More
How to Choose a Proper Technology for the Marketplace Development
February 15, 2018

It is difficult to decide on proper technology choice for the web and mobile marketplace creation nowadays. Great B2B or B2C marketplace development ideas require great ‘under-the-hood’ contents/composition. Let’s consider what technologies fuel up top marketplace platforms of different types.
Read More
Frontend vs Backend Web Development
February 24, 2017

When searching for web development jobs, you’ll find a wide variety of requirements. Languages, frameworks, and methodologies may differ, but there are two aspects of web development that will be common for all jobs: frontend and backend.
Read More
What Is a Framework?
July 13, 2018

Understanding Open-Source Libraries & Frameworks Frameworks are like jet packs for development languages: They boost performance, extend capabilities, and offer…
Read More
Sections

    Admin Support Community Customer Stories Customer Support Data Design Education Enterprise Solutions Finance For Clients For Freelancers Legal Marketing Mobile Development Starting Up Trends Web Development 

Additional

    Blog Authors Submit An Article Sign Up For Email Post a Job Resources 

Company Info

    About Us
    Press
    Careers
    Upwork Blog
    Terms of Service
    Privacy Policy
    Hiring Headquarters
    Quarterly Skills Index
    Trust & Safety

Additional Services

    Enterprise Solutions
    Upwork Pro
    Local Business Resources

Connect with us

    Contact & Support
    API Center

Browse

    Freelancers by Skill
    Freelancers in USA
    Freelancers in UK
    Freelancers in Canada
    Freelancers in Australia
    Find Jobs

Follow us

© 2015 - 2018 Upwork Global Inc.

    1
    1
    6
    3
    0
    3

