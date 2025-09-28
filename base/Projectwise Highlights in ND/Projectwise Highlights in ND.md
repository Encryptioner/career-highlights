# Projectwise Highlights in ND

Created: August 3, 2025 11:03 AM
Date: December 31, 2025
Tags: Special Entry

**Projectwise Highlights** of [Mir Mursalin Ankur’s](https://encryptioner.github.io/) work in [Nerddevs Ltd](https://www.nerddevs.com/)

*Last Updated: September 01, 2025*

---

**Table of Contents:**

---

# Overall Journey (2019 - 2025)

Throughout my career, I have consistently embraced challenges and pursued excellence across a wide range of technologies and domains. From ERP systems to mobile apps, and from legacy systems to greenfield projects, I have consistently chosen tools and approaches that are best aligned with business needs. My journey has taken me from Software Engineer to Lead Software Engineer, marked by both technical growth and leadership development.

I have led teams on high-impact projects, architecting scalable solutions serving 200k+ users, guiding development from concept to production, and establishing modern technology stacks that became the foundation for future initiatives. My work has spanned industries—from travel and education to energy and government—where I’ve delivered impactful solutions such as gas field automation, school management platforms, and large-scale reporting systems.

Beyond delivery, I’ve championed automation and productivity, introduced CI/CD pipelines, and built tools to streamline workflows. I’ve invested in knowledge sharing through mentorship, technical sessions, and blogs, while fostering collaboration, setting standards, and learning from peers.

At the core, my focus has always been on building maintainable, impactful solutions that create real business value—while growing alongside the people and teams I work with.

---

# Shopify CRM Chat (2025 - Present)

**Contribution Overview:** As team lead, guided the project from start to finish. Divided the tasks between members and did R&D for an optimal approach. Earlier, we wanted to integrate WhatsApp for Chat. But later, due to api pricing and setup complexity, using AI seems feasible.

- **Key Tools**
    - **Language/Monorepo**: TypeScript 5, Node.js 22, PNPM workspaces
    - **Shopify**: @shopify/shopify-api, @shopify/shopify-app-express, App Bridge (React), Polaris UI, Shopify CLI, Liquid theme extension
    - **Backend**: Express, MongoDB (Mongoose), Socket.IO, OpenAI SDK, AWS S3/CloudFront, JWT, rate limiting, compression, Winston logging
    - **Frontend (Admin)**: React 18, React Router 7, TanStack Query 5, Vite 5, Axios, i18next, Polaris Icons
    - **Storefront Widget**: React 18, Vite 7 (SWC), Tailwind CSS, PostCSS, React Icons
    - **Shared Packages**: DTOs with class-validator/class-transformer, shared types
    - **Tooling/Quality**: ESLint 9 (flat, TS), Prettier 3, Stylelint Polaris, tsx, concurrently, PM2
    - **Infra/Ops**: Docker, Shopify TOML configs, PM2 configs

### Storefront (Extension)

- **Highlights**
    - **Highlights of 2025**
        - **Chat Widget**: Built a sample chat widget extension for customer interactions.
        - **AI Integration**: Worked on chat backend with testing and streaming response support.
        - **MCP Integration & Documentation:** Added support for Bitbucket MCP integration and updated documentation for further use.

### Admin (Embedded App)

- **Highlights**
    - **Highlights of 2025**
        - **Project Setup**: Initialized app template and cursor rules.
        - **File Upload**: Implemented file upload system for AI training.
        - **Knowledge Base:** Implemented options to modify the knowledge base and change training data.

---

# Biddaan (2025 - Present)

**Contribution Overview:** As team lead, I modified the existing project to make it a company product, supporting a broader audience in a scalable manner. Designed multi-company support, subscription plan tied with feature toggle, and seamless delivery. Provided decision on product features and UI/UX flow, and maintained the bridge between the development team, marketing team, and support team while focusing on business objectives.

- **Key Tools**
    - **Core Stack:** TypeScript, Node.js, Express, Vue 3
    - **Frontend:** Vue CLI (webpack), Pinia, Vue Router, Tailwind CSS + DaisyUI, Sass, Vee-Validate + Yup
    - **UI/UX add-ons:** Chart.js + vue-chartjs, Quill/TinyMCE, MathQuill/KaTeX, Swiper, intl-tel-input
    - **Backend:** Express, Mongoose (MongoDB), Passport + JWT, Multer, Morgan, express-rate-limit, Puppeteer (Automation)
    - **Queues/Cache:** BullMQ with ioredis
    - I**ntegrations:** AWS S3 + CloudFront, Mailgun, Google APIs, Puppeteer
    - **i18n & Analytics**: vue‑i18n, GTM plugin
    - **Build Tooling:** Modular Monolith, pnpm workspaces, Vue CLI Service, Gulp 4 (clean-css, uglify, imagemin, webp, autoprefixer), dotenv(-webpack)
    - **Dev/CI:** ESLint (Airbnb + TS + Vue), TypeScript, Nodemon, PM2, Docker + docker-compose, Bitbucket Pipelines, concurrently
    - **Logging/Observability:** Winston (+ daily rotate, MongoDB transport)
    - **Utilities:** axios, lodash, dayjs, nprogress, html-to-text
- **References**
    - **Promotional Website:** https://biddaan.com/?lang=bn
    - **Public/Student Portal:** [https://dev.biddaan.com/](https://dev.biddaan.com/)
    - **Admin Portal:** [https://sub.domain.biddaan.com/](https://sub.domain.biddaan.com/)

### Public (Full-Stack Website)

- **Highlights**
    - **Highlights of 2025**
        - **Package Updates and AI Support**: Maintained and updated dependencies to stay up to date. Designed marking quizzes with AI support.
        - **Type Safety**: Implemented comprehensive TypeScript type definitions for i18n and API responses.
        - **Performance Optimization**: Enhanced memory management and added monitoring for production systems.
        - **Internationalization**: Expanded multi-language support with backend translation keys and error handling.
        - **Bitbucket Integration**: Added MCP server integration for enhanced development workflow.

### Admin (Full-Stack Website)

- **Highlights**
    - **Highlights of 2025**
        - **Subscription plan tied to feature toggle:** Designed subscription plan with feature toggle for continuous delivery of new features.
        - **SEO Management**: Implemented comprehensive SEO handling system for companies with student portals.
        - **Company Payment System**: Developed company payment history and management features with subscription plans.
        - **Dynamic Fields**: Enhanced dynamic field system with company-wise filtering and deletion capabilities.
        - **CI/CD & Scripting:** Designed multiple pipelines for dev and production deployment and maintained scripts for build, nginx setup, and more.

### Promotional (Static Website)

- **Highlights**
    - **Highlights of 2025**
        - **SEO & Analytics Implementation**: Integrated Google Tag Manager, canonical URLs, robots.txt, sitemap generation, and comprehensive SEO optimization for better search engine visibility and analytics tracking.
        - **Infrastructure & Deployment**: Set up Bitbucket CI/CD pipelines, PM2 process management, S3/CloudFront serving, and automated deployment workflows for production and staging environments.
        - **UI/UX Enhancements**: Redesigned hero sections, updated navigation, improved responsive design, added testimonials, and implemented a modern portfolio-style project showcase with proper branding and contact information.
        - **Performance Optimization & CDN Integration**: Enhanced website loading speed through WebP image conversion, CloudFront CDN integration, image optimization, and build script improvements for a better user experience.
        - **Multi-Language Support**: Developed complete Bengali language support with language switching functionality, font weight optimization, and localized content for the entire website, including navigation, footer, and all major sections.

---

# BD Gas (2024 - 2025)

**Contribution Overview:** As team lead, analyzed complex manual gas field reporting processes across multiple fields. A comprehensive automation solution was later proposed in a presentation following numerous meetings with the client. When budget constraints emerged, we successfully adapted to deliver a hybrid reporting system that enhanced existing Excel workflows while adding multi-admin capabilities and automated reporting features for Bangladesh's gas field operations.

- **Key Tools**
    - **Core Stack**: TypeScript, Node.js, Express, Vue 3, pnpm workspaces
    - **Frontend**: Vue CLI (webpack 5), Pinia, Vue Router, Tailwind CSS + DaisyUI, Sass, GTM plugin, Vee‑Validate, Yup
    - **Data**: MongoDB (Mongoose), Redis
    - **Excel & Automation**: .NET 8 (ClosedXML/OpenXML), BullMQ (job queue/scheduler)
    - **Cloud & Files**: AWS S3 (AWS SDK v3, presigned URLs)
    - **Email**: Mailgun, Handlebars, html‑to‑text
    - **Logging**: Winston, winston-daily-rotate-file, winston-mongodb
    - **Tooling/DevOps**: pnpm workspaces, Docker/Docker Compose, PM2, ESLint, Bitbucket Pipelines
    - **Code Structure**: Modular Monolith, class‑validator, class‑transformer, module‑alias, reflect‑metadata
- **References**
    - **Admin Website:** [https://sub.domain.nerddevs.com/](https://sub.domain.nerddevs.com/) ****
    

### Admin (Full-Stack Website)

- **Highlights**
    - **Highlights of 2025**
        - **Excel Sheet Generation & Management**: Developed comprehensive Excel sheet generation system with .NET integration for gas field data processing, including reference sheet validation and multiple sheet upload capabilities.
        - **Data Entry System Enhancement**: Built robust daily data entry forms for multiple gas fields (Bakhrabad, Habiganj, Meghna, Titas, Narsingdi) with role-based access control and validation.
        - **Admin Dashboard & Reporting**: Implemented an advanced admin dashboard with real-time report status, download functionality, and role-based navigation for operation admins and site admins.
        - **Queue Management & Error Handling**: Developed a sophisticated queue handling system for Excel processing with proper error handling, loading states, and file management for production stability.
        - **Reference Sheet Validation**: Created an intelligent reference sheet validation system that handles missing sheets gracefully and provides proper error messaging for first-of-month scenarios.
    - **Highlights of 2024**
        - **System Analysis & Proposal**: Conducted a comprehensive analysis of the existing manual Excel-based gas field reporting system and designed a fully automated solution supporting multiple gas fields and admin roles.
        - **Architecture Design**: Proposed modular system architecture with Super Admin and Admin sections, including mock UI designs for data entry, reporting, and multi-field management capabilities.
        - **Adaptive Solution**: Successfully pivoted from a full automation proposal to a hybrid solution when budget constraints emerged, delivering reporting features on top of the existing Excel system with multi-admin support.

---

# AI Chat Bot (2024)

**Contribution Overview:** Architected and developed a scalable AI chat interface that enables multiple companies to deploy intelligent customer support bots across their websites.  Designed a robust admin dashboard for companies to manage their AI training data, monitor performance, and customize bot behavior. Implemented secure multi-tenant architecture with automated deployment pipeline, handling critical scalability challenges to support diverse website integrations.

- **Key Tools**
    - **Core Stack**: TypeScript, Node.js, pnpm workspaces
    - **Frontend**: Vue 3, Pinia, Vue Router, Tailwind CSS + DaisyUI
    - **Forms & Validation**: Vee‑Validate, Yup
    - **Backend**: Express, CORS, Multer, JWT, Rate Limiting
    - **Realtime**: Socket.IO
    - **Data & storage**: MongoDB; AWS S3
    - **AI & External APIs**: OpenAI SDKs, Google APIs
    - **Build & Bundling**: Webpack 5, PostCSS/Autoprefixer, Sass Loader, esBuild
    - **Dev Tooling**: ESLint (Airbnb base, Vue, Tailwind), Nodemon, TSConfig
    - **CI/CD & Runtime**: Bitbucket Pipelines (S3 deploy, CloudFront invalidate, SCP to server), PM2 (process manager)
- **References**
    - **AI Mate Chat Bot:** [https://dev.aimate.online/](https://dev.aimate.online/)
    - **Nerddevs Chat Bot:** [https://nerddevs.com/](https://nerddevs.com/)
    - **Admin Website:** [https://sub.domain.aimate.online/](https://sub.domain.aimate.online/)

### Bot (Full-Stack Website)

- **Highlights**
    - **Highlights of 2024**
        - **Embeddable Chat Widget Development**: Built a complete embeddable AI chat interface that can be integrated into any website using a simple script tag.
        - **Real-time Chat Architecture**: Implemented WebSocket-based real-time messaging system with conversation history management, authentication, and company-specific chat isolation.
        - **CSS Isolation & Performance Optimization**: Developed shadow DOM implementation to prevent CSS conflicts with host websites and optimized script loading for faster chatbot initialization.
        - **Production Deployment & DevOps**: Set up comprehensive deployment pipeline with PM2 process management, Docker containerization, and AWS S3/CloudFront integration for scalable production hosting.
        - **UI/UX Enhancements & Component Architecture**: Created modular Vue.js components with loading states, notification systems, chat history management, and responsive design for seamless user experience across different websites.

### Admin (Full-Stack Website)

- **Highlights**
    - **Highlights of 2024**
        - **AI Training System Development**: Built comprehensive AI model training infrastructure with checkpoint support, job status tracking, and validation systems for company-specific training data management.
        - **Admin Dashboard Enhancement**: Developed advanced responsive admin interface with JSON viewer, training data formatting, and company-wise data filtering capabilities for better data visualization and management.
        - **Database & Security Implementation**: Implemented root admin creation on database initialization and enhanced the authentication system with proper user role management and security protocols.
        - **Company Query Management**: Created automated company queries update script with cyclic dependency resolution for efficient data synchronization across the platform.
        - **Full-Stack Architecture**: Contributed to building monorepo architecture with Vue.js frontend, Express.js backend, MongoDB database, properly linted TypeScript, comprehensive testing, and deployment pipeline.

---

# FT Education (2023 - 2025)

**Contribution Overview:** As team lead, assessed the client's requirements after meetings, and designed the project proposal from the start. Later, took a key role in task estimation, assignment, delivery, and deployment. Managed dev & production server with efficiency. At peak, the project served over 80k students and 10+ admins monthly.

- **Key Tools**
    - **Core Stack**: TypeScript, Node.js, Express, Vue 3, pnpm workspaces
    - **Frontend**: Vue CLI (webpack 5), Pinia, Vue Router, Tailwind CSS + DaisyUI, Sass, GTM plugin, Vee‑Validate, Yup
    - **Editors & Math**: Quill, TinyMCE, MathType, MathQuill, KaTeX
    - **Charts & media**: Chart.js + vue‑chartjs, Swiper, Video.js
    - **Backend**: Express, Mongoose (MongoDB), Passport + JWT, bcryptjs, Multer, Morgan, express‑rate‑limit, Puppeteer (Automation)
    - **Storage & Email**: AWS S3, CloudFront, Mailgun, Handlebars, html‑to‑text
    - **Logging**: Winston (+ daily rotate, MongoDB transport)
    - **Build & Linting**: Vue CLI Service, TypeScript (tsc), ESLint (Airbnb + TS + Vue), cpy‑cli
    - **Dev & Ops**: Nodemon, PM2, Docker + docker‑compose, Bitbucket Pipelines, concurrently
    - **Code Structure**: Modular Monolith, class‑validator, class‑transformer, module‑alias, reflect‑metadata
    - **Utilities**: axios, lodash, dayjs, mitt, nprogress, dotenv(-webpack)
- **References**
    - **Public/Student Portal:** [https://ft.education/](https://ft.education/)

### Public (Full-Stack Website)

- **Highlights**
    - **Highlights of 2025**
        - **Project Export:** Helped export the project to a different team.
        - **Deployment:** Support handling DDOS attacks and manage server load.
    - **Highlights of 2024**
        - **Coupon & Bundle Course Support**: Implemented coupon support for course payment and handling bundle courses.
        - **Exam System**: Developed complete quiz/exam platform with scoring, leaderboards, and time-based assessments.
        - **Cloud Infrastructure**: Integrated signed and unsigned AWS CloudFront for content delivery and S3 for file storage.
        - **Dynamic Content**: Built company-specific configurations and dynamic page management system.
        - **SEO Optimization**: Enhanced search engine optimization with meta tags and structured data.
    - **Highlights of 2023**
        - **Core Platform Development**: Built foundational education platform with user authentication, course management, and payment systems.
        - **UI/UX Implementation**: Developed responsive landing pages, navigation systems, and mobile-friendly interfaces.
        - **Payment Integration**: Implemented SSL Commerz payment gateway with confirmation workflows and refund policies.
        - **Course Management**: Created course enrollment, material access, and bundled course functionality.
        - **SMS/OTP System**: Built comprehensive SMS verification system with rate limiting and user bypass features.

### Admin (Full-Stack Website)

- **Highlights**
    - **Highlights of 2025**
        - **Multi-Company Architecture**: Implemented comprehensive company isolation system across all modules.
        - **Style and View Configuration:** Implemented isolated theme and style configuration for different companies handled via CloudFront public file for faster access.
    - **Highlights of 2024**
        - **Content Admin and Question Bank:** Specialized admin role was created to handle the question bank, upload questions to support easy quiz creation.
        - **Company Cache System**: Built caching mechanism for company data to improve performance.
        - **Sub Programs and YouTube Courses:** Implemented sub programs for courses and handled showing YouTube courses categorically by fetching the playlist.
        - **Dynamic Routes & Pages**: Developed configurable route popups and an editable route management system to show specialized pages for courses.
        - **Answer Sheet Marking**: Created marking system for marker admins with answer sheet management.
    - **Highlights of 2023**
        - **Student Management**: Built comprehensive student list with filtering, enrollment tracking, and Facebook group approval integration.
        - **Enrollment System**: Developed enrollment list with date filters, course filtering, and detailed student information.
        - **Course Management**: Implemented course update functionality with price management and validation.
        - **Profile Management**: Added profile image upload to S3 with instructor profile enhancements.
        - **UI/UX Improvements**: Updated styling, navigation, and responsive design across the application.

---

# PixelsCraft (2023 - 2025)

**Contribution Overview:** Led PixelsCraft from concept to a premium App Store release across iPhone and iPad. Engineered high‑quality image generation with OpenAI through careful prompt design and tuned API parameters, then added effortless community sharing and cross‑app export. Defined and implemented backend and admin systems—subscriptions and a reusable template pipeline—to support scale and predictable operations. 

Elevated quality by mentoring junior developers, formalizing QA, triaging issues, and shipping performance and UX improvements. Managed App Store releases end‑to‑end and authored guidelines for promotional visuals and videos to streamline marketing. Navigated AI model transitions and broadened generation controls to preserve output quality while expanding creative range.

- **Key Tools**
    - **Core Stack**: TypeScript, Node.js 18, pnpm workspaces
    - **Backend**: Express, CORS, Multer, File Processing
    - **Data & Jobs**: MongoDB, Mongoose, Redis, BullMQ
    - **Auth & Security**: Passport, passport-jwt, passport-anonymous, JSON Web Token, bcryptjs, express-rate-limit
    - **Cloud & Storage**: AWS SDK S3, S3 presigner
    - **AI & External APIs**: OpenAI, Google APIs, Google Auth Library, App Store Server API, Mailgun
    - **Logging**: Winston, winston-daily-rotate-file, winston-mongodb, Morgan, debug
    - **Frontend Web (Admin)**: Vue 3, Vue CLI, webpack, Vue Router, Pinia, Tailwind CSS + DaisyUI, Vee-Validate, Yup
    - **Mobile App Stack**: Flutter, Dart, Firebase Analytics, Firebase Core, Firebase Messaging, Firebase Remote Config, in_app_purchase, in_app_review
    - **Mobile Device & Media**: HTTP, connectivity_plus, shared_preferences, get, get_storage, image_picker, image_cropper, flutter_local_notifications, url_launcher, video_player, cached_network_image
    - **Build & Tooling**: TypeScript ESLint, Airbnb config, Jest, Vue Test Utils, ts-jest, dotenv-webpack, PostCSS, Sass, Madge, Nodemon
    - **CI/CD & Runtime**: Bitbucket Pipelines, SCP deploy, AWS S3 deploy, CloudFront invalidate, PM2
- **References**
    - Promotional Website: https://app.pixelscraft.io/
    - App Store: https://apps.apple.com/us/app/pixelscraft/id6471664167
    - Admin Website: [https://sub.domain.pixelscraft.io/](https://sub.domain.pixelscraft.io/)

### App (Cross-Platform App)

- **Highlights**
    - **Highlights of 2025**
        - **Multi-AI Model Architecture Planning**: Designed and planned implementation strategy for supporting multiple AI models to enhance image generation capabilities and user choice.
        - **Technical Leadership & Mentorship**: Guided fellow developers through implementation phases, conducted code reviews, and provided technical direction for feature development.
        - **Quality Assurance & Optimization**: Performed comprehensive testing, UI/UX reviews, and suggested performance improvements to enhance app responsiveness and user experience.
    - **Highlights of 2024**
        - **Subscription Management Enhancement**: Fixed subscription verification issues and improved purchase flow with better user feedback.
        - **Platform Updates**: Updated Flutter SDK requirements and maintained compatibility with the latest platform versions.
        - **iOS Release Preparation**: Updated iOS build configurations and version management for App Store deployment.
        - **Performance Optimization**: Improved app performance and resolved platform-specific issues for both Android and iOS.
        - **Version Management**: Maintained consistent version control and build management across multiple releases.
    - **Highlights of 2023**
        - **Project Foundation & Core Features**: Built the initial Flutter app structure with chat functionality, conversation management, and AI integration for image generation.
        - **Firebase Integration**: Implemented comprehensive Firebase services, including messaging, analytics, remote config, and background message handling.
        - **In-App Purchase System**: Developed a complete subscription management system with purchase verification, restore functionality, and user credit tracking.
        - **UI/UX Development**: Created responsive design with tablet support, implemented chat interface, conversation history, and image gallery with pagination.
        - **Cross-Platform Optimization**: Configured Android and iOS builds, implemented platform-specific features like image downloading and sharing.

### App (Backend)

- **Highlights**
    - **Highlights of 2025**
        - **Advanced AI Features**: Enhanced image generation with support for multiple AI models, background removal, image editing, and advanced quality controls.
        - **Subscription System Enhancement**: Improved subscription management with sandbox testing, better error handling, and enhanced purchase verification.
        - **Performance Optimization**: Implemented file upload improvements, memory optimization, and enhanced API response handling for better scalability.
        - **Template Management**: Developed sophisticated image template system with version filtering, user preferences, and dynamic content generation.
        - **Production Stability**: Focused on bug fixes, performance improvements, and maintaining production stability with comprehensive logging and monitoring.
    - **Highlights of 2024**
        - **AI Image Generation Core**: Developed the main AI image generation system with DALL-E integration, image upload/editing APIs, and credit-based usage system.
        - **Subscription & Payment Integration**: Implemented Apple App Store and Google Play Store subscription systems with server-side verification and purchase history tracking.
        - **Basic API Architecture**: Created foundational REST APIs for user operations, conversation management, and template handling with proper error handling and validation.
        - **Production Infrastructure**: Established comprehensive production deployment with Docker, Redis caching, MongoDB optimization, and monitoring systems.
    - **Highlights of 2023**
        - **Project Foundation & Initial Setup**: Established the core backend infrastructure with Node.js, Express, MongoDB, and Redis. Set up Docker containerization, PM2 process management, and initial project structure.
        - **User Management System**: Implemented comprehensive user authentication without registration, which ties to the user’s device.
        - **Database Schema Design**: Designed MongoDB schemas for users, conversations, templates, and subscription data with proper indexing and relationships.
        - **Development Environment**: Configured development tools, linting, TypeScript setup, and deployment pipeline with Bitbucket integration.

### Admin (Full-Stack Website)

- **Highlights**
    - **Highlights of 2025**
        - **Template Versioning**: Added support for versioning image templates.
        - **Schema/Model Hardening**: Refined schema and model for stability.
        - **CI Reliability**: Enforced strict pnpm version in Bitbucket pipelines.
    - **Highlights of 2024**
        - **AI & Templates**: Updated OpenAI models; improved template token handling and related naming cleanup.
        - **Code Quality & Repo Hygiene**: Removed unused code/APIs; key renames; app/project name updates; .gitignore and README refinements.
    - **Highlights of 2023**
        - **Push Notifications (end-to-end)**: Implemented APNs/Firebase, logging, scripts, iOS config, and CRUD UI.
        - **CI/CD & Runtime ops**: Designed Bitbucket pipelines, PM2 config, SCP deployment, pnpm upgrades.
        - **Release/Version Controls**: Managed min/current app versions via settings; schema-driven defaults; backend/FE validation; required field indicators.
        - **Storage & Media**: Integrated AWS S3 in backend; added client media file API support.
        - **User/Auth improvements**: Overhauled user types/schema, improved auth service and routing, enhanced user listing/pagination.

---

# AI Mate & AI Seek (2023 - 2025)

**Contribution Overview:** As lead for AI Mate and AI Seek, set direction and delivered outcomes as usage surpassed 200k+ users. Under a tight deadline, shipped the first Flutter mobile MVP despite no prior Flutter background—establishing tickets, coding standards, and release cadence. Architected the app and resolved complex issues in socket communication, state management, and performance. Implemented Play Store and App Store subscriptions, then extended the strategy to web—linking identities across platforms and adding web subscriptions to avoid vendor lock‑in.

Introduced real-time AI audio chat and matured it through iterative testing and telemetry. Later, aligned the web experience with mobile, enabling cross‑platform account linking and consistent entitlements. Launched the AI Seek variant focused on reasoning, reusing proven patterns to accelerate delivery and reduce maintenance.

- **Key Tools**
    - **Core Stack**: TypeScript, Node.js 18, pnpm workspaces, Vue 3, Flutter (Dart)
    - **Backend**: Express, EJS, CORS, JWT, Multer, Rate Limit
    - **Data & Queues**: MongoDB, Mongoose, Redis, BullMQ
    - **Realtime**: Socket.IO, OpenAI Realtime API
    - **Cloud & Storage**: AWS SDK S3, S3 presigner, Firebase Admin
    - **Payments & Subscriptions**: Paddle Node SDK, Paddle JS, App Store Server API, Google Play Billing Library, Flutter In-App Purchase
    - **AI & External APIs**: OpenAI, Google APIs, Google Auth Library, gaxios
    - **Logging & Monitoring**: Winston, winston-daily-rotate-file, winston-mongodb, Morgan, debug
    - **Web Frontend Stack**: Vue CLI (webpack 5), Vue Router, Pinia, Vee-Validate, Yup, GTM
    - **Styling & UI**: Tailwind CSS, DaisyUI, Swiper, nprogress, highlight.js
    - **Mobile App Stack**: GetX, get_storage, shared_preferences, http, socket_io_client, image_picker, image_cropper, video_player, open_file, path_provider, permission_handler
    - **Mobile Voice & Realtime**: flutter_webrtc, speech_to_text, flutter_tts, flutter_sound, audio_session
    - **Build, Testing & Tooling**: ESLint (TypeScript, Airbnb), PostCSS, Sass, Nodemon, PM2, Bitbucket Pipelines
- **References**
    - **Website:** [https://app.aimate.online/](https://app.aimate.online/)
    - **Play Store:** https://play.google.com/store/apps/details?id=com.aimate.app
    - **Admin Website:** [https://sub.domain.aimate.online/](https://sub.domain.aimate.online/)

### App (Cross-Platform App)

- **Highlights**
    - **Highlights of 2025**
        - **YouTube Transcript Ingestion**: Added YouTube transcript service and test rollout.
        - **Multi-AI Model & Realtime Audio Chat Architecture Planning**: Designed and planned implementation strategy for supporting multiple AI models and handling real-time audio chat.
        - **Technical Leadership & Mentorship**: Guided fellow developers through implementation phases, conducted code reviews, and provided technical direction for feature development.
        - **Quality Assurance & Optimization**: Performed comprehensive testing, UI/UX reviews, and suggested performance improvements to enhance app responsiveness and user experience.
        - **Play Store Release:** Designed Play Store release and reviewed objections to handle different restrictions and rules updates.
    - **Highlights of 2024**
        - **Image-enabled Chats**: Sent images as byte strings; handled text-only/image flows; regenerated response support.
        - **Favorites & Home UX**: Redesigned home page with template favorites toggle and sorted templates.
        - **Release Engineering**: Maintained iOS setup and Podfile management; Android/iOS version/build bumps; SDK/lockfile consistency.
        - **Quality & Safety**: Ensured type fixes, function arg bugfixes, log cleanup, clearer conditions, and state handling.
        - **Subscription/UX polish**: Introduced the terms button in the subscription page and dynamic refinements of color/icon/UI.
    - **Highlights of 2023**
        - **Core Chat Platform**: Implemented conversation history/detail, socket streaming, regenerate replies, and countdown timers with robust error handling.
        - **Subscription & Restore**: Shipped purchase/restore flows, backend sync, shared storage, and cross-device sync without registration.
        - **Firebase & Notifications**: Added messaging, device tokens, background handlers, and Remote Config-driven features.
        - **Cross-Platform Releases**: Managed Android/iOS versioning, Podfile/Gradle updates, App Store assets/docs, and OS compatibility.
        - **UX & Performance**: Deployed skeleton loaders, dark mode/theming, iconography, share/export, and file handling, plus timeouts/retries for optimization.

### Public (Full-Stack Website)

- **Highlights**
    - **Highlights of 2025**
        - **Realtime Chat Platform**: Added input audio transcription, session time limits, and saving realtime chats under conversation threads.
        - **Audio Quality & Controls**: Introduced input noise reduction and feature flag to enable/disable real-time API usage.
        - **Model Compatibility**: Updated model names/aliases and handling across app versions; aligned with the latest OpenAI package.
        - **YouTube Transcript Ingestion**: Enabled YouTube caption/transcript fetching and client-side support for transcript-based processing.
        - **API/Data Hardening**: Improved schema and payload handling, refined DTOs and projections for real-time flows.
    - **Highlights of 2024**
        - **Web Subscriptions (Paddle)**: Implemented checkout, product listing, cancel, upgrade, and payment method updates with webhook verification and customer sync.
        - **Model Lifecycle & UX**: Set sensible default config, removed deprecated models, improved model selection UI/logic.
        - **AI Chatbot on Web**: Deployed/iterated the site chatbot widget with lazy loading and conditional rendering.
        - **Conversation Archiving**: Optimized storage to keep only necessary fields and refined delete handling.
        - **Template Features & Gating**: Added favorites, version-gated templates (e.g., YouTube), and reduced non-stream conversation code.
    - **Highlights of 2023**
        - **Core Chat System**: Built conversation creation/resume, streaming over Socket.IO, chat history with infinite scroll, message utilities, and code snippet rendering.
        - **App–Web Account Linking**: Added app login via token, TTL verification codes, link user API, and UX updates for linked accounts.
        - **Mobile Subscriptions (Apple/Google)**: Implemented verification via App Store/Google Developer APIs, server notifications, restore flows, and subscription history/types.
        - **Formatting & Templates**: Introduced input/output formatting configs, preview types (markdown/html/xml), export options, and template-driven conversation settings (e.g., max tokens).
        - **Observability & Performance Telemetry**: Implemented execution logger, standardized OpenAI error logs, and per-request timing (requesting/processing/saving) to diagnose latency and improve reliability.
        - **Client Setup & CI/CD**: Initialized Vue client, responsive navigation, and CI/CD (S3/CloudFront, pipelines), plus server static serving iterations.

### Admin (Full-Stack Website)

- **Highlights**
    - **Highlights of 2025**
        - **Realtime Chat Admin Controls**: Introduced admin-side controls for real-time chat (enable/disable, session time) and UI improvements.
        - **CI/CD Hardening**: Upgraded pnpm and streamlined build pipeline for reliable releases.
        - **Release Orchestration**: Coordinated multiple releases and dev and prod merges
    - **Highlights of 2024**
        - **User Usage Analytics Dashboard**: Built user usage reporting with filters (date ranges, platform), totals, and default sorting.
        - **Conversation Insights**: Shipped conversation list and user-level conversation modal for deeper visibility.
        - **Data Table UX & Performance**: Enhanced lazy-loaded tables with per-table selection and helper component updates.
        - **LLM Model Lifecycle**: Updated OpenAI conversation models, set default configs, and removed deprecated models.
    - **Highlights of 2023**
        - **Platform Foundation & Schema**: Bootstrapped codebase, integrated schemas, user types, and default projections.
        - **Push Notification System (E2E)**: Implemented admin creation/mutation, queues with Redis, APNs/iOS support, and operational scripts.
        - **DevOps & Automation**: Set up Bitbucket pipelines (incl. client build), PM2 config, and streamlined deploys (SCP).
        - **Cloud Storage & Media**: Integrated AWS S3 and media APIs; added AWS setup and client support.
        - **Admin & UX Enhancements**: Designed version management (min/current), user pagination, conversation template I/O, and type sync with backend.

---

# Genius (2022 - 2024)

**Contribution Overview:** Led development of a full-stack web/app platform from MVP to growth stage under tight deadlines. Bootstrapped from existing boilerplate and modernized to the latest standards. Designed task allocation, established development workflows, and maintained code quality through PR reviews. Managed development and production environments efficiently. The platform successfully scaled to serve over 100k+ users with robust performance and reliability.

- **Key Tools**
    - **Core Stack**: Node.js, TypeScript, pnpm workspaces
    - **Backend Framework & Middleware**: Express, CORS, Multer, JWT,  Morgan, Winston, winston-daily-rotate-file, winston-mongodb, @parse/node-apn
    - **Realtime & Caching**: Socket.io, @socket.io/redis-adapter, ioredis
    - **Data Layer**: MongoDB, Mongoose
    - **Cloud & Storage**: AWS SDK S3, S3 Request Presigner
    - **AI/LLM (backend)**: OpenAI SDK, tiktoken, gpt-3-encoder
    - **File & Document Processing**: pdfjs-dist, mammoth, word-extractor, xml2js, csvtojson, json2csv, form-data
    - **Queues & Scheduling (admin)**: BullMQ, node-cron, ioredis
    - **Frontend (admin)**: Vue 3, Vue Router 4, Pinia, Pinia Persisted State, Vee-Validate, Yup, Tailwind CSS, DaisyUI, Heroicons
    - **Frontend Build Tooling (admin)**: @vue/cli-service, Webpack 5, Babel, PostCSS, dotenv-webpack, PWA plugin, browser polyfills
    - **CI/CD & Ops**: Bitbucket Pipelines, Atlassian SSH Run, AWS S3 Deploy, AWS CloudFront Invalidate, PM2, Docker Compose
- **References**
    - **App Store:** https://apps.apple.com/us/app/ai-chat-5-0-genius/id1665764663
    - **Admin Website:** [https://sub.domain.genius.io/](https://sub.domain.genius.io/)

### App (Backend)

- **Highlights**
    - **Highlights of 2024**
        - **Multi-format File Ingestion**: Implemented text extraction services for PDF, DOC/DOCX, PPTX, and TXT with extension checks and updated dependencies.
        - **Extractor Architecture Refactor**: Generalized the extraction function, reorganized ExtractDataFromFile, and removed unnecessary packages/files.
        - **Model Configuration UX**: Added preferred/default/free model selection, returned available models on demand, and updated settings schema/types.
        - **Logging Polish**: Improved logs and minor refactors for readability and consistency.
        - **Conversation Hygiene**: Streamlined deletion and archived only necessary conversation data.
    - **Highlights of 2023**
        - **Conversation Platform Foundation**: Created/resumed conversations, template support with response max tokens, streaming responses, validation (length/punctuation), and bubble messaging.
        - **Subscription & Billing**: Integrated Google Play Developer API verification (timeouts, retries), managed subscription status/history, CSV purchase reporting, and RevenueCat timeout handling.
        - **Observability & Reliability**: Added execution/time profiling (OpenAI/backend), structured error logging, improved logger formatting, and robust timeout/header handling.
        - **Infrastructure & Pipelines**: PM2 configs, Bitbucket pipeline, Redis docs/config, queue/jobs improvements (push notifications, scheduling), and repo/module alias/route updates.
        - **User/Auth/Settings**: User creation/auth flows with custom errors, unique code service, default projections, settings schema defaults, device/platform fields, contact/email modules, pagination/DTOs, and trimmed payload validation.

### Admin (Full-Stack Website)

- **Highlights**
    - **Highlights of 2024**
        - **New Model Integration & Release**: Planned and merged new AI models across services to expand AI capability and choice.
        - **Model & Config Hardening**: Updated model configs, removed unused constants, and simplified redundant settings declarations.
        - **Type-safety & Validation Polish**: Tightened types, validations, and UI consistency for admin workflows.
        - **Feature Controls**: Introduced visibility control for limits to simplify UX and experimentation.
        - **Dependency Hygiene**: Updated lockfile and performed small stability/cleanup tasks.
    - **Highlights of 2023**
        - **Project Bootstrap & Architecture**: Initial integration from boilerplate, removal of legacy/unnecessary code, standardized package naming, and module structure setup.
        - **Storage & Media Pipeline**: Integrated AWS S3 on backend and added client-side media file API support.
        - **User & Auth Domain**: Designed user types/schema, refactored auth service, improved unique-code handling, and separated server vs client routes.
        - **Admin Settings Governance**: Added minimum/current version controls, backend/frontend validations with required indicators, and default-from-schema behavior.
        - **Push Notification System (end-to-end)**: Built admin create/edit/list, added Redis/BullMQ queues and workers, device-token ingestion, scheduling/time controls from admin, and improved logging/observability.

---

# Second Line & Second Text (2022 - 2025)

**Contribution Overview:** Spearheaded the panoramic modernization of a decade-old legacy codebase (2014-present), handling 50+ GB of data volume. Implemented TypeScript migration, established ESLint standards, upgraded database infrastructure, and eliminated deprecated APIs and unnecessary code. Successfully delivered new features while transitioning the system from legacy architecture to modern deployment practices. The modernization effort improved maintainability and positioned the text/call platform for continued growth on Apple devices.

- **Key Tools**
    - **Core Stack**: Node.js 18, TypeScript, npm scripts
    - **Web Framework**: Express, body-parser, cookie-parser, morgan, serve-favicon
    - **Database**: MongoDB, Mongoose
    - **Queues and Jobs**: Bull, Agenda, Redis
    - **Realtime**: Socket.io, socket.io-redis
    - **Messaging/Telephony**: @bandwidth/messaging, node-bandwidth
    - **Notifications/Email**: @parse/node-apn, mailgun-js
    - **Search**: @elastic/elasticsearch
    - **File Handling**: Multer, fast-csv, csvtojson, json2csv, file-type, read-chunk, node-stream-zip, archiver, node-unzip-2
    - **Monitoring/APM**: Datadog, Spam Detection, dd-trace, winston, winston-daily-rotate-file
    - **Utilities**: class-validator, class-transformer, string-cosine-similarity
    - **Testing/Quality**: Jest, Mocha, Chai, chai-http, ESLint, @typescript-eslint, eslint-config-airbnb, eslint-watch, @html-eslint, Stylelint, stylelint-config-standard, stylelint-scss
- **References**
    - **Second Line App Store:** [https://apps.apple.com/us/app/second-line-2nd-phone-number/id1459896638](https://apps.apple.com/us/app/second-line-2nd-phone-number/id1459896638)
    - **Second Text App Store:** [https://apps.apple.com/us/app/second-texting-number/id1274216319](https://apps.apple.com/us/app/second-texting-number/id1274216319)
    - **Second Line Admin**: [https://sub.domain.line.second.io/](https://sub.domain.line.second.io/)
    - **Second Text Admin:** [https://sub.domain.text.second.io/](https://sub.domain.text.second.io/)

### App (Backend)

- **Highlights**
    - **Highlights of 2025**
        - **Call Information Management**: Implemented comprehensive call info storage system with spammer call ratio tracking and enhanced logging mechanisms for better call analytics.
        - **Code Quality Enhancement**: Introduced auto-linting processes and cleaned up unnecessary files while maintaining proper documentation standards.
        - **System Monitoring**: Enhanced log message systems and direction-finding capabilities for improved debugging and system maintenance.
    - **Highlights of 2023**
        - **Architecture Modernization**: Migrated entire application to Node.js version 18 with updated package dependencies and enhanced ESLint rules for better code quality.
        - **Admin-Backend Separation**: Successfully separated admin functionality from backend services, removing unnecessary client-side components and organizing API routes for better maintainability.
        - **Docker Integration**: Implemented comprehensive Docker support with proper configuration, documentation, and the ability to run backend without database dependencies.
        - **API Cleanup & Organization**: Massive refactoring effort removing deprecated v1 APIs, organizing route structures, and separating admin vs end-user API endpoints.
        - **Client-Side Removal**: Complete removal of client-side React components, bower references, and static file serving to streamline backend-only architecture.
    - **Highlights of 2022**
        - **Docker Infrastructure**: Added complete Docker support with compose files, startup configurations, and debugging capabilities for containerized deployment.
        - **Spam Detection Enhancement**: Implemented advanced spam detection features with new database columns and improved user management loading states.
        - **Authentication System**: Fixed and enhanced password reset functionality from email with improved error handling and user experience.
        - **Contact System Foundation**: Built comprehensive contact management system with robust error handling, testing infrastructure using Faker and crypto libraries.
        - **Testing Framework**: Established proper testing patterns with environment variable management and comprehensive test coverage for contact functionality.
        - **Documentation & Error Handling**: Implemented systematic documentation updates and enhanced error handling mechanisms across contact-related features.

### Admin (Full-Stack Website)

- **Highlights**
    - **Highlights of 2025**
        - **Anti-Spam Enhancement**: Implemented call ratio tracking in anti-spam rules and system settings with default field configurations for improved spam detection.
        - **Admin User Management**: Added sample admin user creation functionality with enhanced login page routing documentation and system configuration improvements.
        - **Documentation Enhancement**: Updated HTML comments, fixed typos, and improved README documentation for a better developer experience and system understanding.
    - **Highlights of 2023**
        - **Admin Architecture Separation**: Massive architectural refactoring to separate admin functionality from the main backend, including API prefix standardization (/admin) and route reorganization for better service isolation.
        - **TypeScript Migration**: Complete migration of server-side components to TypeScript, including startup files, route handlers, logger, helper utilities, and database connection modules for better type safety.
        - **Docker Integration & Infrastructure**: Implemented comprehensive Docker support with containerization, database independence options, PM2 configuration, and detailed documentation for streamlined deployment.
        - **API Cleanup & Modernization**: Extensive removal of unnecessary APIs across all modules (users, billing, messages, subscriptions, etc.), organized route structures, and eliminated deprecated endpoints for cleaner architecture.
        - **Job Scheduling Removal**: Eliminated unnecessary job scheduling services and related functionalities from the admin interface, simplifying the system architecture and reducing complexity.
    - **Highlights of 2022**
        - **Project Foundation & Setup**: Established complete project infrastructure, including Docker support, admin user creation system, database startup configurations, and comprehensive linting setup for both client and server-side code.
        - **Code Quality Framework**: Implemented extensive ESLint rules, StyleLint integration, client-side linting capabilities, and established coding standards with automated fixing for improved code quality and consistency.
        - **Admin User Management System**: Built a robust admin user creation and management system with password update mechanisms, configuration-based user matching, and system settings handling for secure administrative access.
        - **TypeScript Integration**: Initiated TypeScript migration, starting with server configuration files, database connections, and application startup scripts, laying the foundation for type-safe development.
        - **Documentation & Development Workflow**: Created comprehensive documentation, including Docker setup guides, development commands, testing procedures, and established proper Git workflows with branch management strategies.

---

# Fax App (2024 - 2025)

**Contribution Overview:** Architected initial project setup by adapting existing solutions to rapidly deliver a foundational infrastructure for handling fax from Apple devices. Conducted critical research and development to implement core features, established deployment strategies, and contributed to project delivery through code reviews and technical guidance. Successfully transitioned the platform from concept to production-ready solution with robust infrastructure foundations.

- **Key Tools**
    - **Core Stack**: Node.js 18, TypeScript, pnpm scripts
    - **Architecture**: Monorepo with multiple workspaces (client, server, types, dto, utilities)
    - **Frontend Framework**: Vue 3, Vue Router, Vue CLI
    - **UI/Styling**: TailwindCSS, DaisyUI, Heroicons, Phosphor Icons
    - **State Management**: Pinia, pinia-plugin-persistedstate
    - **Form Handling**: VeeValidate, Yup validation
    - **Backend**: Express, Morgan, cookie-parser, cors
    - **Database**: MongoDB, Mongoose, Redis
    - **Authentication**: Passport, JWT, bcryptjs, Firebase Admin
    - **File Processing**: Multer, AWS SDK S3, CSV processing (csvtojson, json2csv)
    - **Logging**: Winston, winston-daily-rotate-file, winston-mongodb
    - **Dev Tools**: ESLint, TypeScript, Nodemon, Vue CLI tools
    - **Utilities**: Lodash, Axios, dayjs, Lodash

### App (Backend)

- **Highlights**
    - **Highlights of 2024**
        - **Complete Backend Infrastructure Setup**: Established the entire fax application backend from scratch with comprehensive authentication, user management, subscription handling, push notifications, file services, and MongoDB integration
        - **Document File Conversion System**: Implemented LibreOffice-based document conversion service to convert DOCX files to PDF format with proper validation and error handling
        - **Firebase Push Notification Integration**: Set up Firebase push notification service with proper initialization and configuration for mobile app communication
        - **Subscription Management System**: Built comprehensive subscription handling system with Apple and Google Play Store integration, including subscription history tracking and validation services
        - **Package Management & DevOps**: Consistently updated Node.js versions, TypeScript configurations, and resolved package dependencies while maintaining CI/CD pipeline compatibility

### Admin (Full-Stack Website)

- **Higlights**
    - **Highlights of 2024**
        - **Complete Admin Panel Foundation**: Built the entire admin interface from scratch with Vue.js, including user management, push notification controls, settings management, and responsive design
        - **Advanced User Filtering System**: Implemented comprehensive user filtering capabilities, including date-based filtering and enhanced user list management with real-time search functionality
        - **Admin Dashboard Components**: Developed reusable UI components, including data  tables, form helpers, modals, file upload handlers, and pagination systems for efficient admin operations
        - **Settings & Configuration Management**: Created a centralized settings management system allowing administrators to configure application parameters and mobile app configurations
        - **Code Quality & Maintenance**: Implemented automated linting, TypeScript upgrades, and maintained consistent code quality standards across the entire admin platform

---

# Daily Stocks (2021 - 2023)

**Contribution Overview:** Designed and built a comprehensive stock notification system from the ground up, enabling users to receive alerts based on custom criteria. Implemented cross-platform push notifications (web/mobile), managed Play Store deployment, and developed web crawling capabilities. Established a modern technology stack that became the standard foundation for future projects. Led technical guidance for bug-free delivery, managed user systems and reusable components, while maintaining production deployment, proper logging, and code quality standards.

- **Key Tools**
    - **Core Stack**: TypeScript, Node.js 16, pnpm workspaces, Vue 3, Android (Java/Kotlin)
    - **Backend**: Express, CORS, cookie-parser, morgan, express-rate-limit, Multer, Passport, passport-jwt, passport-anonymous, jsonwebtoken
    - **Database**: MongoDB, Mongoose
    - **Queues and Jobs**: BullMQ, Redis
    - **Notifications and Email**: Firebase Admin, web-push, Mailgun.js
    - **Cloud and APIs**: AWS SDK S3, S3 presigner, Google Auth Library
    - **Logging and Monitoring**: Winston, winston-daily-rotate-file, winston-mongodb, debug
    - **Data and File Utilities**: csvtojson, json2csv, file-type, form-data, handlebars, html-to-text, luxon, lodash
    - **Frontend Frameworks**: Vue Router, Pinia, Pinia Persisted State, Vee-Validate, Workbox Precaching, Tailwind CSS + DaisyUI
    - **Frontend Tooling**: Vue CLI Service, Webpack 5, PostCSS, Autoprefixer, Sass, dotenv-webpack, vue-loader
    - **Testing**: Jest, ts-jest, @vue/test-utils, Testing Library jest-dom, @shelf/jest-mongodb, mongodb-memory-server
    - **Android App**: Firebase BoM, Firebase Cloud Messaging, Firebase Analytics, WorkManager, Volley, Gson, AndroidX Core/Activity/Fragment, Material Components
    - **DevOps**: Docker, Docker Compose, Bitbucket Pipelines, PM2
- **References**
    - **Website:** [https://dailystocks.info/](https://dailystocks.info/)
    - **Facebook Page:** [https://www.facebook.com/DailyStocksInfo](https://www.facebook.com/DailyStocksInfo)

### Public (Full-Stack Website)

- **Highlights**
    - **Highlights of 2023**
        - **User Experience Enhancement**: Improved landing page flow with automatic redirection for logged-in users
        - **Visual Identity**: Updated logos, branding elements, and footer components for better brand recognition
        - **Navigation Optimization**: Enhanced routing logic to provide seamless user experience between public and authenticated areas
    - **Highlights of 2022**
        - **Portfolio Management System**: Built complete stock portfolio tracking system with buy/sell history, weighted averages, and P&L calculations
        - **Real-time Stock Alerts**: Implemented stock price monitoring with customizable high/low price notifications
        - **Mobile App Integration**: Created Flutter webview compatibility with notification permissions and authentication
        - **Vue 3 Migration**: Successfully migrated from Vue 2 to Vue 3 with Pinia state management, replacing Vuex
        - **Tailwind CSS Integration**: Rebuilt entire UI with modern Tailwind CSS framework for better responsiveness
    - **Highlights of 2021**
        - **Frontend Architecture**: Implemented Vue as the primary frontend framework
        - **User Registration System**: Created user signup/login functionality with email verification
        - **Responsive Design**: Built mobile-first responsive layouts for cross-device compatibility
        - **Navigation System**: Developed a user-friendly navigation system with a proper routing structure
        - **Email Service Integration**: Set up HTML email templates for user communication

### Admin (Full-Stack Website)

- **Highlights**
    - **Highlights of 2023**
        - **Production Deployment**: Enhanced PM2 configuration for better process management in production environments
        - **Developer Branding**: Added developer attribution and branding components throughout the application
        - **Documentation Updates**: Improved project documentation and deployment instructions
    - **Highlights of 2022**
        - **User Management Dashboard**: Built comprehensive admin panel with user listing, filtering, and search capabilities
        - **Settings Management**: Implemented global application settings with timezone configuration and notification schedules
        - **Email Event Tracking**: Created an email event monitoring system to track delivery status using Mailgun API
        - **Database Optimization**: Added pagination, sorting, and lazy loading for efficient data management
        - **Push Notification Infrastructure**: Developed a complete push notification system with Firebase and web push integration
    - **Highlights of 2021**
        - **Project Foundation**: Established the complete monorepo architecture with Vue 3 frontend and Express backend setup
        - **Development Infrastructure**: Set up TypeScript configuration, ESLint rules, and build pipeline for scalable development
        - **Docker Integration**: Implemented containerization with Docker Compose for streamlined deployment and development
        - **Authentication System**: Built user authentication framework with JWT tokens and password hashing
        - **Code Quality Standards**: Established linting standards, prettier configuration, and package management with proper versioning

### App (Webview App)

- **Highlights**
    - **Highlights of 2023**
        - **Documentation & Repository Management**: Enhanced project documentation with comprehensive setup instructions with detailed Firebase configuration steps, and streamlined the development workflow for better team collaboration and onboarding.
        - **Codebase Maintenance**: Performed essential maintenance updates to ensure compatibility with the latest Android development practices and addressed any technical debt accumulated during the rapid development phase of 2022.
        - **Production Stability**: Focused on ensuring long-term stability and maintainability of the mobile application, addressing any production issues, and optimizing performance based on real-world usage patterns.
    - **Highlights of 2022**
        - **Complete Android WebView Application Architecture**: Built a comprehensive Android WebView application from scratch, providing a native mobile experience with proper navigation and swipe-to-refresh functionality.
        - **Firebase Cloud Messaging Integration**: Implemented complete FCM push notification system with user-specific token management, and seamless integration with the backend API for real-time stock alerts.
        - **Advanced Error Handling & Network Management**: Developed robust error handling with custom error pages, network connectivity detection, automatic retry mechanisms, and user-friendly error dialogs with appropriate fallback strategies.
        - **Production-Ready Build System**: Configured multi-APK generation supporting multiple ABIs, code minification, and resource shrinking for optimized release builds with proper app profiling capabilities for monitoring.
        - **Google Play Store Release:** Manage Play Store release while handling different rules for terms, privacy policy, and Social authentication

### Stock Puller (Backend Service)

- **Highlights**
    - **Highlights of 2023**
        - **Cross-Platform Compatibility**: Enhanced the documentation with Mac-specific installation instructions, ensuring seamless setup across different development environments and improving the developer onboarding experience.
        - **Production Optimization**: Refined deployment configurations and documentation based on real-world production usage, addressing platform-specific issues and streamlining the deployment process for better operational efficiency.
        - **Maintenance & Stability**: Implemented ongoing maintenance updates and bug fixes to ensure continuous service reliability and optimal performance in production environments.
        - **Infrastructure Modernization**: Updated deployment strategies and configuration management to align with modern DevOps practices and ensure scalability for future enhancements.
    - **Highlights of 2022**
        - **Stock News Scraping System**: Architected and implemented a comprehensive stock news scraping service that fetches stock news data, parsing HTML tables to extract trading codes, news titles, and publication dates with proper date range filtering.
        - **Advanced Logging Infrastructure**: Developed a robust logging system with timezone-aware logging, time-based log rotation (midnight rotation with UTC), and centralized error tracking.
        - **Production-Ready Scheduler Service**: Built a sophisticated background job scheduler using APScheduler with cron-based triggers, error handling, graceful shutdown mechanisms, and configurable interval-based stock price pulling.
        - **Containerization & DevOps Pipeline**: Established complete Docker containerization with PostgreSQL database, created Bitbucket CI/CD pipelines for automated deployment, and implemented systemd service configuration for Linux servers.
        - **Error Handling & Reliability**: Implemented comprehensive timeout handling for HTTP requests, connection error management, graceful service degradation, and automatic job queue recovery mechanisms to ensure 24/7 service availability.
        - **API Security & Rate Limiting**: Designed a token-based authentication system for API endpoints, implemented request validation with proper error responses, and established configurable rate limiting to prevent API abuse.
    

---

# Daency (2020 - 2022)

**Contribution Overview:** With a small team, developed a comprehensive online dance collaboration platform during the pandemic, enabling seamless group video streaming for remote learning. Built real-time chat functionality, multi-instructor teaching capabilities, moderator controls with focus and engagement features, and integrated social platform connectivity. Implemented individual practice modes, a session purchasing system, and an admin portal for public management.

Enhanced the platform with advanced features, including AI-powered game scoring, synchronized video playback across all session members, and pixel-perfect Figma design implementation. Established a detailed testing strategy covering unit, integration, and end-to-end testing to ensure platform reliability and seamless user experience across all collaborative features.

- **Key Tools**
    - **Core Stack**: Node.js 14, TypeScript, Yarn workspaces
    - **Frontend**: Vue.js 2, Vue Router 3, Vuex 3, Vuetify 2, Vue CLI 4
    - **Backend**: Express.js, Socket.io, Passport.js, JWT authentication
    - **Database & Caching**: MongoDB, Mongoose, Redis, BullMQ for job queues
    - **Real-time Communication**: Agora RTC SDK 4, PubNub 4, Socket.io for chat and video
    - **Payment Processing**: Stripe 8 for payment gateway integration
    - **Cloud Services**: AWS SDK (S3, Lambda), Mailgun for email, Twilio for SMS/OTP
    - **Authentication**: Google OAuth2, Facebook Login, WeChat Login, JWT tokens, SSO
    - **File Handling**: Multer for file uploads, AWS S3 for storage, video.js for media playback
    - **Development Tools**: Docker 19, Docker Compose, ESLint, Jest for testing, Nodemon
    - **Build & Deployment**: Webpack 4, Vue CLI, Concurrently for parallel processes
    - **UI Components**: Bootstrap 5, Vuetify components, v-emoji-picker, vuedraggable
    - **Utilities**: Lodash, Moment.js, Day.js, Axios for HTTP requests, Winston for logging
    - **Testing**: Jest, Vue Test Utils, MongoDB memory server for testing
    - **DevOps**: Docker containerization, AWS CLI, PM2 for process management
- **References**
    - **Promotional Video:** [https://www.youtube.com/@daency1020](https://www.youtube.com/@daency1020)

### Public (Full-Stack Website)

- **Highlights**
    - **Highlights of 2022**
        - **Messaging & Communication Enhancement**: Implemented unread message flagging system with message preview functionality and improved friend group messaging
        - **Gaming Integration**: Built a comprehensive game scoring system with leaderboards, user count tracking, and game link generation for interactive learning experiences
        - **WeChat Social Login**: Integrated WeChat authentication to expand accessibility for Chinese users
        - **Campaign Redirection System**: Developed smart campaign routing to optimize user engagement flows
        - **Real-time Game Analytics**: Created APIs to show live game participant counts and profile images
    - **Highlights of 2021**
        - **User Profile Enhancement**: Added comprehensive bio sections, social media links integration, and avatar click popups for better user interaction
        - **Elfsight Widget Integration**: Implemented social proof widgets across game lists, activities, and class pages to boost engagement
        - **AI Game Scoring**: Integrated AI-powered game scoring system visible in user activity feeds
        - **Agora SDK Upgrade**: Enhanced video calling capabilities with improved performance and reliability
        - **Second Rotation Video**: Implemented advanced video rotation and port handling for a better mobile experience
    - **Highlights of 2020**
        - **Advanced Video Controls**: Implemented an expansive video player with speed control, volume management, section jumping, and progress tracking
        - **Real-time Classroom Experience**: Built synchronized video watching with live participant indicators and social interaction features
        - **Class Scheduling & Access**: Developed student scheduling system with access code verification and upcoming class notifications
        - **Responsive Classroom UI**: Optimized classroom interface for mobile devices with touch-friendly controls and adaptive layouts
        - **Social Authentication**: Integrated Google and Facebook login with profile image synchronization

### Admin (Full-Stack Website)

- **Highlights**
    - **Highlights of 2022**
        - **Game Management System**: Built bulk game upload functionality, game editing capabilities, and game file management with CORS handling
        - **CSV Upload Improvements**: Enhanced data import capabilities with better validation and error handling
        - **Game Analytics Dashboard**: Implemented game score collection tracking and leaderboard management tools
        - **Content Management**: Developed automated sync systems for game lists and improved file handling processes
    - **Highlights of 2021**
        - **Campaign Management for Games**: Built admin tools to manage game-specific campaigns and promotional content
        - **User Information Backend**: Developed expansive user data management system with enhanced profile fields
        - **Leaderboard Administration**: Created admin controls for game leaderboards and scoring systems
        - **Widget Configuration**: Built backend systems to manage Elfsight widgets across different platform sections
        - **Payment Management:** Integrated Stripe payment management system to create dynamic pricing from the admin dashboard with coupon features
    - **Highlights of 2020**
        - **Class Category Management**: Built comprehensive category and tagging system with validation and bulk operations
        - **Advanced Class Filtering**: Implemented multi-criteria filtering system (paid/free, favorites, categories) with persistent URL states
        - **Video Content Management**: Created video section management tools with thumbnail generation and AWS S3 integration
        - **Analytics & Reporting**: Built class engagement tracking and user activity monitoring systems
        - **Content Upload System**: Implemented drag-and-drop video and image upload with progress tracking and validation

### Game (Frontend)

- **Highlights**
    - **Highlights of 2021**
        - **Game Authentication Integration**: Built seamless login system with visual effects and popup management
        - **Score Posting System**: Implemented real-time score submission with backend integration
        - **Cross-Domain Communication**: Built robust connection between the game UI and the main classroom by developing secure authentication token sharing
        - **User Experience Enhancements**: Added loading visual effects and improved game interaction flows
        - **Code Optimization**: Removed unnecessary files, updated build processes, and improved project structure

---

# Bikribatta (2019 - 2023)

**Contribution Overview:** Modernized a complex legacy codebase while delivering continuous feature enhancements across all project components. Led comprehensive development with a lean team, resolving critical bugs and providing customer support. Successfully expanded the platform to serve heavy feature requirements for end consumers while maintaining operational excellence.

Developed a comprehensive ERP platform covering inventory, accounting, HR, and project tracking. Implemented multi-language support and payment processing while modernizing the frontend architecture. Built scalable multi-company operations with automated workflows that streamlined business processes and enhanced operational efficiency for enterprise clients.

Created a full-stack e-commerce solution integrated with ERP backend, featuring responsive catalogs and payment gateway integration. Delivered mobile-optimized customer experiences that transformed traditional businesses into omnichannel retailers with expanded market reach and streamlined online operations.

Built an offline-capable desktop application enabling complete inventory operations without internet connectivity. Developed synchronization capabilities and point-of-sale functionality, ensuring business continuity during network outages while maintaining data integrity across online/offline modes for uninterrupted business processes.

- **Key Tools**
    - **Core Stack (ERP)**: Node.js 12, Express 4, Vue 2, Yarn, Docker Compose
    - **Backend (ERP)**: Express, Pug, CORS, JWT, Multer, Express Rate Limit
    - **Data (ERP)**: MongoDB 3.2–4.x, Mongoose 4.x
    - **Frontend (ERP)**: BackboneJS, Vue 2, TypeScript 3, Service Worker
    - **Microservices (ERP)**: Go 1.13, MongoDB Driver, go-redis
    - **Cloud/Integrations (ERP)**: AWS SDK, Google APIs, SendGrid, Mailgun
    - **Dev Tools (ERP)**: Grunt, Nodemon, Concurrently, Mocha, Chai
    - **Views & Templating (E-Commerce)**: Pug, Handlebars
    - **Payment Gateway (E-Commerce)**: SSLCommerz
    - **Core Stack (Offline)**: Electron 1.6, electron-builder, Node 8, Express 4, RequireJS, Bower
    - **Data/Offline Sync (Offline)**: NeDB, RxDB, PouchDB adapters, Mongoose 5.5
    - **Realtime/Auth (Offline)**: Socket.io 2, express-jwt, Passport, Passport-Local
    - **UI Toolkit (Offline)**: jQuery, Bootstrap, Backbone, DataTables, Select2, Dropzone, iziToast
    - **Core Stack (App)**: Android Gradle Plugin 7.3.1, Kotlin 1.7.20, Gradle 7.5.1
    - **Tools (App)**: Firebase BOM 31.3, Analytics, Material Components, WorkManager, ViewBinding, ProGuard/R8, ABI splits, MultiDex
- **References**
    - **Promotional Website:** [https://bikribatta.com/](https://bikribatta.com/)
    - **ERP Website:** [https://sub.domain.bikribatta.com/](https://sub.domain.bikribatta.com/)

### ERP (Full-Stack Website)

- **Highlights**
    - **Highlights of 2023**
        - **Vue 3 Migration**: Led frontend modernization by migrating the ERP system to Vue 3 with updated ESLint configurations and development tooling
        - **Framework Integration**: Implemented Vue.js project integration within Backbone.js framework using iframe architecture for modular ERP components
        - **Code Quality Enhancement**: Updated ESLint rules and VSCode settings to improve code quality and development experience across the ERP codebase
        - **Configuration Management**: Enhanced configuration management by extracting base URL data from config files for better environment handling
        - **Development Tooling**: Streamlined CLI commands and development workflow improvements for the ERP application
    - **Highlights of 2022**
        - **Project-Based ERP Architecture**: Implemented comprehensive project-wise functionality across all major ERP modules, including stock management, reporting, and financial operations
        - **Advanced Stock Management**: Developed project-wise stock adjustment reports, product consumption tracking, and inter-project material transfer capabilities
        - **Financial System Enhancement**: Added project tracking to payment vouchers, supplier payments, and voucher management with comprehensive project-based filtering
        - **Comprehensive Reporting System**: Created project-wise reports for daily activities, stock analytics, receive analytics, supply ledger, and product ledger
        - **Inventory Control Optimization**: Enhanced stock transfer functionality with project-to-project transfers, validation systems, and real-time inventory updates
    - **Highlights of 2020**
        - **Payment Gateway Integration**: Implemented online payment system with session management, payment confirmation, and automatic voucher generation
        - **Multi-Language Support**: Developed comprehensive internationalization (i18n) framework with Bangla language support for company-specific localization
        - **Advanced ERP Reporting**: Created dynamic table reporting system with configurable settings, JSON-based report generation, and CSV export capabilities
        - **Barcode Management System**: Built product barcode generation with customizable settings, multiple format support, and company-specific configurations
        - **Customer Relationship Management**: Enhanced customer management with SMS integration, template systems,  message tracking, and mobile number validation
        - **HR/Payroll System**: Implemented company-wide HRM and payroll functionality with sms/slack notifications, Google Calendar integration and salary management
    - **Highlights of 2019**
        - **Product Variant Management**: Developed comprehensive product variant system with CSV upload, filtering, and inventory tracking capabilities
        - **Financial Accounting Enhancement**: Implemented trial balance, income statement, balance sheet reports with account opening balance management
        - **Advanced Inventory Features**: Created product ledger, supplier ledger, sales order tracing, and comprehensive stock reporting with date filtering and analytics
        - **Attendance Management System**: Built complete HR attendance tracking system with IP address validation, remote login controls, and comprehensive reporting
        - **Gross Profit Analytics**: Developed detailed gross profit reporting Cost of Goods Sold (COGS) analysis for business intelligence
        - **Dashboard Analytics**: Created comprehensive dashboard with top customers, product performance metrics, and real-time business KPIs
        - **Accounting System Enhancement**: Developed voucher management system with automatic generation, cancellation workflows, and company-specific templates
        - **User Permission Management**: Built granular permission system for different user roles with menu and action-based access control

### E-Commerce (Full-Stack Website)

- **Highlights**
    - **Highlights of 2022**
        - **Frontend Architecture Modernization**: Enhanced e-commerce frontend components with improved stock management interfaces and project-based filtering capabilities
        - **Payment System Enhancement**: Integrated project-based payment processing for e-commerce orders with enhanced frontend payment workflows
        - **Order Management Optimization**: Improved order processing system with project-wise categorization and enhanced order tracking capabilities
    - **Highlights of 2020**
        - **Payment Gateway Integration**: Implemented complete online payment system with session key management, payment confirmation, redirect URLs, and automatic collection entry for paid orders
        - **Advanced Cart & Checkout Management**: Built sophisticated cart functionality, including price calculations, VAT display, delivery charges, shipping address, and easy checkout
        - **Customer Management Enhancement**: Implemented e-commerce customer support, mobile number validation, automatic customer creation, and customer-specific cart handling
        - **Order Processing System**: Created complete order management system with order details display, status tracking, payment type filtering, and order confirmation workflows
        - **Product Variant Support**: Added complete product variant management for e-commerce with available quantity tracking and variant-specific pricing
    - **Highlights of 2019**
        - **Complete E-commerce Foundation**: Built the entire e-commerce platform from scratch, including frontend architecture, backend API integration, and database schema design
        - **Product Catalog System**: Developed comprehensive product catalog with filtering, search functionality, pagination, image galleries, and product detail pages with zoom effects
        - **Shopping Cart Implementation**: Created full shopping cart functionality with add/remove items, quantity management, cart persistence, and cart detail views
        - **Multi-level Navigation**: Implemented sophisticated menu system with categories, subcategories, quick catalog, and breadcrumb navigation
        - **Order Management Foundation**: Built order processing system with order validation, email notifications, SMS integration, and order history tracking
        - **Promotional Features**: Developed dynamic image sliders, promotional item displays, featured products, marketing content management, and different theme outlooks
        - **Mobile Responsiveness**: Created a mobile-optimized e-commerce experience with touch navigation, responsive layouts, and mobile-specific styling

### Offline (Software)

- **Highlights**
    - **Highlights of 2020**
        - **Synchronization Architecture Enhancement**: Implemented advanced sync mechanisms for collection data after sale creation with improved data consistency
        - **Image Processing Pipeline**: Created sophisticated image upload and processing systems with duplicate detection and error handling
        - **Hardware Authentication Framework**: Enhanced offline hardware validation system with multi-level authentication protocols
        - **Data Import/Export Optimization**: Improved bulk upload processes for product catalogs with image support, enhanced error reporting, and validation
        - **Offline Sales Reporting**: Developed comprehensive offline sales analytics with status tracking and performance metrics
    - **Highlights of 2019**
        - **Complete Offline Application Architecture**: Built entire offline inventory management system using Electron framework with NeDB local database
        - **Advanced Synchronization System**: Implemented bidirectional data sync between offline app and server with conflict resolution and retry mechanisms
        - **Hardware Registration & Authentication**: Developed comprehensive hardware verification system with unique device identification and access control
        - **Offline Sales Management**: Created complete offline point-of-sale system with quick sales, collection management, and receipt printing
        - **Local Database Implementation**: Integrated NeDB for local data storage with models for customers, products, sales, and collections
        - **Real-time Data Upload/Download**: Built automated sync modules for seamless data exchange between offline and online systems

### Promotional (Static Website)

- **Highlights**
    - **Highlights of 2020**
        - **SEO and Metadata Enhancement**: Implemented comprehensive SEO improvements, including updated meta tags, Open Graph properties, and structured data for better search engine visibility and social media sharing.
        - **Customer Feedback Integration**: Developed and implemented a customer feedback system, replacing the previous SoftExpo section, including video pop-up functionality with enhanced user engagement features.
        - **Visual Asset Management**: Added preview images, play buttons, and customer feedback media assets to improve the website's visual appeal and user interaction capabilities.
        - **UI/UX Enhancement**: Redesigned the website layout with improved CSS styling, responsive design updates, and better visual hierarchy to enhance user experience across different devices.

### ERP (Webview App)

- **Highlights**
    - **Highlights of 2022**
        - **Complete Android App Architecture**: Initialized and built a comprehensive Android app from scratch with WebView implementation for BikriBatta mobile application.
        - **UI/UX Enhancement**: Updated application icons, color schemes, spacing, and visual elements to align with BikriBatta brand identity and improve user interface consistency.
        - **Development Infrastructure**: Set up expansive project structure with Gradle configuration, ProGuard rules, and release APK management
        - Google Play Store Release: Set up Google Play Store profile, managed debug and release APK for the first time.

---

# BD Traffic Police (2019 - 2020) & (2023)

**Contribution Overview:** Developed two comprehensive mobile and web applications for the Bangladesh Traffic Police under tight deadlines with evolving requirements. Built a traffic case management system featuring a React Native mobile app with Bangla number plate recognition and automated SMS notifications for violations.

Created an accident database system with detailed incident forms serving as a comprehensive vehicle database. Implemented extensive charting capabilities to visualize accident patterns, providing valuable insights for traffic safety analysis and policy decisions to help reduce accidents across Bangladesh.

- **Key Tools**
    - **Core Stack (App)**: React Native, React, NativeBase, React Navigation
    - **State and Networking (App)**: Redux, React Redux, Redux Thunk, Axios
    - **Device Capabilities (App)**: react-native-camera, react-native-fs
    - **Mobile UI/UX Utilities (App)**: react-native-modal-overlay, react-native-phone-input, react-native-root-toast, react-native-table-component
    - **Mobile Testing/Build (App)**: Jest, babel-jest, react-test-renderer, Gradle bundling scripts
    - **Backend Service (App)**: @google-cloud/vision, @google/maps, Bangla text detection
    - **Backend Core**: Express, CORS, Body-Parser, Cookie-Parser, Morgan, Pug
    - **Service Testing/Dev**: Mocha, Chai, Chai-HTTP, Nodemon, Winston
    - **Authentication/Rate Limiting**: JSON Web Token, express-rate-limit
    - **Database Layer**: MongoDB, Mongoose
    - **Notifications**: SendGrid (E-mail), Reve SMS

### Traffic Case (Cross-Platform App)

- **Highlights**
    - **Highlights of 2023**
        - **Android SDK Modernization**: Updated compile SDK version, build configurations, and React Native compatibility issues to ensure compatibility with the latest Android versions and security requirements, maintaining app store compliance.
        - **Build System Enhancement**: Resolved React Native linking errors, updated package dependencies, and fixed Gradle build issues to ensure smooth compilation and deployment processes.
        - **Trial Period Management**: Updated fixed trial period dates and configurations to maintain controlled access and demo functionality for new users and testing environments.
        - **Documentation and Project Maintenance**: Updated documentation with current installation instructions and project setup guidelines, ensuring new developers can easily onboard to the project.
        - **Bundle and Asset Management**: Regenerated Android bundle files after Gradle builds, ensuring optimized app performance and proper asset inclusion for production releases.
    - **Highlights of 2020**
        - **Backend Integration and Server Migration**: Successfully migrated authentication from the local system to dev server, removing over 1,000 lines of legacy package management code and streamlining the application architecture.
        - **Geolocation and Vision Integration**: Implemented expansive location and vehicle tracking system by automatic GPS coordinate capture and license number detection from image.
        - **SMS Notification System**: Developed automated SMS sending functionality on case confirmation, enhancing communication between traffic authorities and violators for improved case processing workflow.
        - **Release Build Optimization**: Created production-ready APK builds with architecture-specific optimizations, universal APK support, and proper release configurations for Google Play Store deployment.
        - **Error Handling and User Experience**: Enhanced error notification systems, empty date handling, and UI improvements, including yellow box disabling for better user experience and application stability.
    - **Highlights of 2019**
        - **Case Management System Development**: Built comprehensive case entry functionality with driver negative point tracking, total fine calculations, and appearance date management for traffic violation cases.
        - **Registration and License Integration**: Implemented driving license entry and registration systems with auto-population features from inquiry data, streamlining data entry processes for traffic officers.
        - **User Interface Enhancement**: Developed home search functionality with registration buttons, table view improvements, and case inquiry menu system for better user navigation and data visualization.
        - **Trial Period Implementation**: Added demo trial period functionality with expiration date management, ensuring controlled access to the application features.
        - **Case Details and Navigation**: Implemented case detail viewing system where users can select case IDs from tables to view comprehensive case information, improving case tracking workflow.

### Traffic Case (Backend + Admin Website)

- **Highlights**
    - **Highlights of 2020**
        - **Traffic Case Management System**: Developed complete traffic case entry backend with comprehensive case tracking, including accused person details, vehicle information, driving license integration, and geolocation support.
        - **Mobile App Integration**: Created login endpoints and API integration specifically for traffic mobile applications, enabling field officers to access the system through mobile devices for real-time case entry and management.
        - **Database Integration and API Development**: Built complete backend infrastructure with models, controllers, and routes for traffic case management, integrating driving license and vehicle registration systems for automated data population.
        - **Officer Case Assignment**: Built a role-based case assignment system allowing traffic cases to be assigned to specific officers with proper authorization and tracking capabilities.
        - **SMS-based Case Query System**: Developed mobile SMS integration allowing citizens to query case information by sending text messages, with automated responses containing case details and status updates.
        - **Case Reporting and Analytics**: Implemented daily case report generation functionality, allowing traffic departments to get summaries of cases entered on specific dates for administrative reporting purposes.
    

### Traffic Accident (Full-Stack Website)

- **Highlights**
    - **Highlights of 2020**
        - **Accident Report Preview System**: Implemented preview functionality for accident reports with formatted templates, allowing officers to review and verify accident data before final submission to authorities.
        - **Accident Analytics and Reporting**: Built sophisticated accident summary and statistics system with statistical summaries and geographical breakdown
        - **Vehicle Confiscation Tracking**: Added vehicle database to track vehicle confiscation statistics in accident reports
        - **Accident Entry Extensions**: Enhanced accident entry forms with improved validation, CSS optimization, responsive UI, and better user experience
        - **Interactive Accident Reporting**: Implemented comprehensive accident reporting system with statistical summaries and geographical breakdown
    - **Highlights of 2019**
        - **Accident Entry Management**: Built frontend and backend infrastructure for accident data collection, including image upload functionality for accident documentation
        - **Officer Integration**: Developed officer details integration in accident entry forms with officer ID-based lookup system
        - **Accident Report Generation**: Created accident report preview templates and selection forms for generating various accident reports
        - **Language Localization**: Implemented multi-lingual support for Bengali users

---

# Demo (2022 - 2023)

**Contribution Overview:** Designed and delivered multiple rapid MVP prototypes for client demonstrations under tight deadlines, overcoming complex architectural challenges, including real-time lip sync with avatar systems. Successfully deployed functional, visually appealing, and maintainable applications that provided effective beta user experiences for prospective clients seeking quick prototyping solutions.

- **Key Tools**
    - **Core Stack**: TypeScript, Node.js 18/16, pnpm/yarn workspaces
    - **Monorepo Packages**: dto, types, utilities
    - **Frontend Frameworks**: Vue 3, Vue 2, Vue CLI
    - **Frontend State & Routing**: Pinia, Vuex, Vue Router
    - **UI & Styling**: TailwindCSS, DaisyUI, Vuetify, Sass
    - **Backend**: Express, EJS, Passport, JWT, bcryptjs, express-rate-limit
    - **Data Layer**: MongoDB, Mongoose
    - **Queues & Realtime**: BullMQ, ioredis, Socket.IO
    - **Cloud & External APIs**: AWS SDK S3, Firebase Admin, Google Cloud Text-to-Speech, OpenAI, App Store Server API, Mailgun
    - **Logging & Monitoring**: Winston, winston-daily-rotate-file, winston-mongodb, morgan
    - **Build & Dev Tools**: Vue CLI Service, Webpack, PostCSS, concurrently, nodemon, ESLint

### 2023: Voice Over ChatGPT (Full-Stack Website)

- **Highlights**
    - **Highlights of 2023**
        - **Platform Foundation**: Built the complete monorepo architecture with TypeScript packages, including a modular structure with proper linting, build configurations, and workspace management
        - **ChatGPT Conversation API Integration**: Implemented comprehensive ChatGPT integration with create/resume chat functionality, history management, and intelligent response handling with configurable token limits
        - **Lip Sync & Video Generation Service**: Developed a Python-based lip sync service integrated with Replicate API for generating synchronized video content from audio inputs, including proper configuration management and file handling
        - **Multi-modal Conversation Support**: Added audio input processing for chat conversations with text-to-speech capabilities and intelligent language switching between English and other languages
        - **Personalized AI Interaction**: Configured ChatGPT to act as a "friend" rather than an assistant, implemented specific question filtering and bypass mechanisms, and added contextual conversation flow management
        - **Production Deployment Configuration**: Added process management, environment configuration examples, proper logging infrastructure, CI/CD pipeline, and necessary documentation for proper build
        - **Mobile View Enhancements**: Implemented mobile-specific hover and click effects, repositioned mode buttons for better mobile UX, and optimized sidebar navigation for smaller screens
    

### 2022: Health App (Full-Stack Website)

- **Highlights**
    - **Highlights of 2022**
        - **Patient Symptom Management System**: Developed expansive patient symptom tracking system with database integration, CRUD operations (create, edit, delete), and symptom population functionality for healthcare providers.
        - **Doctor-Patient Interface**: Built patient detail viewing system for doctors with popup dialogs, patient symptom display, and role-based access control to show appropriate information based on user roles.
        - **Print & Export Functionality**: Implemented patient symptom printing capabilities with styled output, delayed window closing for proper printing, and enhanced print formatting for medical documentation.
        - **Full-Stack Patient API**: Created complete backend API infrastructure for patient management, including routes, DTOs, database models, and endpoints for patient symptom data retrieval and management.
        - **Deployment & DevOps Integration**: Added Bitbucket pipeline for CI/CD, configured backend to serve frontend files, implemented route handling for single-page application deployment, and enhanced logo/branding updates.
        - **Authentication & User Management**: Implemented user registration system with email verification, HTML email templates, role-based access control, and admin/doctor role differentiation with appropriate redirects.
    

---

# Boilerplate (2020 - Present)

**Contribution Overview:** Architected and developed comprehensive boilerplate solutions across multiple technology stacks, including React Native, Vue.js, Node.js, and TypeScript, establishing enterprise-grade foundations with modern development standards, automated testing pipelines, and streamlined deployment workflows. Delivered maintainable starter kits featuring advanced user management, real-time chat systems, subscription handling, and social authentication, enabling rapid project bootstrapping with consistent code quality and documentation standards across mobile and web platforms.

- **Key Tools**
    - **Core Stack**: Node.js 18-20, TypeScript, Flutter/Dart, React Native, pnpm/yarn scripts
    - **Web Frameworks**: Express, Vue 3, Vue CLI
    - **Mobile Frameworks**: Flutter SDK (cross-platform), React Native (Android)
    - **Database**: MongoDB 4-7, Mongoose, Redis, IORedis
    - **UI/Styling**: TailwindCSS, DaisyUI, Phosphor Icons, React Native Paper
    - **State Management**:
        - Web: Pinia, pinia-plugin-persistedstate
        - Mobile: GetX, Redux, React Redux
    - **State Management**: Pinia, GetX, pinia-plugin-persistedstate
    - **Authentication**: Passport, JWT, bcryptjs, Google OAuth2, Facebook API
    - **Real-time**: Socket.io, Socket.io Redis adapter, Socket.io Client
    - **Mobile Features**: Firebase (Core, Messaging, Analytics, Remote Config), Apple Store Server API, Push notifications, In-App Purchases, Camera & Geolocation Service
    - **Form Handling**: Vee Validate, Yup validation, class-validator, class-transformer
    - **File Processing**: Multer, AWS SDK S3, HTML-to-text, JSON-2-CSV
    - **Background Jobs**: BullMQ 3-5
    - **Email**: Mailgun.js, Handlebars templating
    - **Logging**: Winston, winston-daily-rotate-file, winston-mongodb, Morgan
    - **Dev Tools**: ESLint, TypeScript, Nodemon, Madge, Docker, Docker Compose, pnpm/yarn workspaces, Gradle
    - **Testing**: Jest unit testing, Flutter Lints
    - **Utilities**: Lodash, Axios, dayjs, Nanoid, Slugify, NProgress, Swiper.js
    - **Analytics**: Google Tag Manager integration
    - **Storage**: Get Storage, SharedPreferences, Local/Session Storage

### Mobile App Backend

- **Highlights**
    - **Highlights of 2024**
        - Designed the approach to create a boilerplate from an existing project for later use
        - Added commands, scripts, and pipelines  for consistent monorepo management
        - Updated linting for a cleaner dev loop

### Mobile App Admin  (Full-Stack Website)

- **Highlights**
    - **Highlights of 2024**
        - **Mobile App Admin Boilerplate Foundation**: Initial project setup and configuration with TypeScript support, establishing the foundational architecture for the mobile app admin interface.
        - **Package Modernization & TypeScript Enhancement**: Updated TypeScript-related packages and package versions, implementing modern development standards and dependency management practices.
        - **Advanced User Management System**: Implemented comprehensive user filtering capabilities, including date-based filtering, search keyword enhancements, and user list management features for improved admin functionality.
        - **Development Infrastructure & Code Quality**: Established auto-lint fixes, updated Node.js versions for compatibility, resolved server-side type errors, and configured deployment pipelines for streamlined development workflow.
        - **Boilerplate Documentation & Configuration**: Enhanced documentation with boilerplate information, updated mobile app name configurations, and implemented proper settings management for easy project customization.

### Vue - Node - Typescript  Public (Full-Stack Website)

- **Highlights**
    - **Highlights of 2024**
        - **Simplified Frontend Setup**: Established a lightweight client architecture with essential components, responsive design, and optimized build processes
    - **Highlights of 2023**
        - **Package Management Modernization**: Migrated from Yarn to PNPM, updated Node.js versions, and streamlined dependency management
        - **User Interface Enhancements**: Refined user profile management, improved social login user experience, and enhanced error handling
    - **Highlights of 2022**
        - **Complete Frontend Migration to Vue 3 & Tailwind**: Migrated entire frontend from Vue 2 to Vue 3 with Tailwind CSS integration, modern responsive design, and improved component architecture
        - **Social Authentication Integration**: Implemented Google login, social media authentication, and profile management with avatar handling
        - **Enhanced User Experience**: Added contact forms, privacy policy pages, terms of service, and comprehensive user dashboard functionality
        - **Security & Performance**: Implemented rate limiting for contact emails, CORS configuration, and performance optimizations
    - **Highlights of 2021**
        - **Frontend Foundation with Vue.js**: Set up initial Vue.js frontend with Vite configuration, component architecture, and modern build tooling
        - **User Authentication System**: Implemented complete user registration, login, email verification, and password recovery workflows

### Vue - Node - Typescript  Admin (Full-Stack Website)

- **Highlights**
    - **Highlights of 2024**
        - **Modern Client Boilerplate Architecture**: Created new streamlined client boilerplate with TypeScript, Vue 3, and modern tooling configuration
    - **Highlights of 2023**
        - **Backend Infrastructure Refinement**: Updated database architecture to MongoDB v6, improved server configurations, and enhanced admin authentication flows
        - **Code Quality & DevOps**: Implemented comprehensive ESLint rules, TypeScript upgrades, automated testing pipelines, and CI/CD improvements
    - **Highlights of 2022**
        - **Comprehensive Testing Infrastructure**: Implemented unit testing, integration testing, and end-to-end testing with Jest, including mock services and database testing utilities
        - **Advanced User Management**: Built sophisticated user list management with filtering, pagination, and admin controls for user operations
        - **Settings & Configuration Management**: Created a centralized settings management system, allowing administrators to configure application parameters
    - **Highlights of 2021**
        - **Full-Stack Admin Infrastructure Setup**: Established complete backend infrastructure with MongoDB integration, authentication controllers, user management, and admin dashboard foundation
        - **Backend Architecture & Services**: Built comprehensive server-side architecture with authentication services, file handling, email services, and database schema design

### Mobile App (Cross-Platform App)

- **Highlights**
    - **Highlights of 2023**
        - **Real-time Chat Streaming System**: Implemented comprehensive stream response functionality for conversations using socket connections, enabling real-time message delivery with proper error handling, timeout management, and retry mechanisms.
        - **In-App Purchase & Subscription Management**: Developed complete subscription system including in-app purchase integration, Firebase Remote Config for product IDs, subscription status tracking, and restore purchase functionality.
        - **Chat Application Core Features**: Built foundational chat application with conversation management, message history, regenerate response functionality, chat detail views, and proper navigation flow between different chat contexts.
        - **Firebase Integration & Push Notifications**: Integrated Firebase services, including authentication, remote configuration, push notification handling with background/foreground support, and device token management.
        - **Mobile App Optimization & Performance**: Implemented app performance improvements, including slow startup fixes, API timeout handling, connectivity checks, skeleton loading screens, error page enhancements, and Android version compatibility.

### Android Starter Kit (Android App)

- **Highlights**
    - **Highlights of 2020**
        - **TypeScript Integration Architecture**: Implemented comprehensive TypeScript integration into the Android starter kit, modernizing the development stack with type safety and enhanced developer experience.
        - **Live Update System Development**: Developed live update functionality for the Android application, enabling real-time content updates and dynamic feature deployment without app store releases.
        - **Project Architecture Refinement**: Applied minor fixes and optimizations to improve overall project stability and performance following the TypeScript migration.
    - **Highlights of 2019**
        - **Authentication System Enhancement**: Implemented logout menu functionality and improved authentication error handling with proper error state clearing for better user experience.
        - **React Native Framework Modernization**: Updated Flow configuration to the latest version and updated the application bundles to ensure compatibility with the latest React Native standards.
        - **Initial Project Architecture:** Designed the project architecture with teammates to support the latest tools and approach for a modern mobile app boilerplate.

---

# Various (2022 - Present)

**Contribution Overview:** Worked on multiple projects on a short-term basis. Mostly for R&D, debugging, and deployment-related tasks. Some of the projects were solo, some as team lead, and on some worked as a consultant. My contribution boosted the projects to reach their goal.

- **Key Tools**
    - **Core Stack**: Node.js 12-18, TypeScript, JavaScript ES6+, npm/yarn, WordPress
    - **Web Frameworks**: Express.js, NestJS, React 16, EJS templating, HTML
    - **Blockchain**: Hardhat, Solidity 0.8.1, Ethers.js, Alchemy Web3, OpenZeppelin
    - **Database**: MongoDB, Mongoose, AWS S3
    - **UI/Styling**: Bootstrap 4, TailwindCSS, Material-UI, Reactstrap, SCSS/Sass
    - **Build Tools**: Webpack 4, Babel, PostCSS, Terser, HTML Webpack Plugin
    - **State Management**: Redux, Redux-Thunk, Redux-Logger
    - **Testing & Quality**: Mocha, Chai, ESLint (Airbnb), Prettier, TypeScript strict
    - **Third-Party APIs**: Stripe, AWS SDK, Google Analytics, Mailchimp, DocuSign, Google Maps
    - **Security**: Helmet, bcryptjs, JWT, Express-validator, Express-session
- **References**
    - **Pithy Engineering Website:** [https://pithyengineering.com/](https://pithyengineering.com/)

### R&D: NFT Starter (Blockchain App)

- **Highlights**
    - **Highlights of 2022**
        - **TypeScript Migration & Architecture Modernization**: Led a complete project transformation from JavaScript to TypeScript, implementing proper ESLint configuration, TypeScript config, and modern development tools.
        - **NFT Metadata & Token Management System**: Developed a comprehensive NFT metadata management system by creating structured example tokens, organizing metadata files into a dedicated tokens directory, and implementing proper IPFS integration for decentralized storage with Pinata support.
        - **Multi-Network Blockchain Integration**: Configured robust support for multiple Ethereum networks (mainnet, Ropsten, Goerli, Rinkeby) with proper environment variable management, Alchemy API integration, and comprehensive documentation for different testnets and deployment strategies.
        - **Developer Experience & Documentation Enhancement**: Created an extensive document covering the complete NFT development lifecycle, from smart contract deployment to minting processes, including third-party integrations, wallet setup instructions, and network-specific scanner links for transaction monitoring.
        - **Smart Contract Development & Deployment Pipeline**: Built a complete Hardhat-based development environment with automated deployment scripts and configuration management, establishing a solid foundation for NFT development workflows.

### Deployment: Pithy Engineering (Full-Stack Website)

- **Highlights**
    - **Highlights of 2025**
        - **Full-Stack Web Application Architecture**: Quickly grasped a complete NestJS-based admin panel application with TypeScript, Tailwind CSS, EJS templating, and modern web technologies, where authentication guards, file upload capabilities, caching mechanisms, and security features were implemented.
        - **CI/CD Pipeline Implementation**: Developed sophisticated Bitbucket Pipelines configuration for automated deployment with SSH-based server management, parallel execution support, and custom deployment triggers.
        - **Production Deployment Infrastructure**: Established an expansive production deployment pipeline with PM2 process management and NGINX with SSL certificate.
        - **Package Management Modernization**: Migrated the project from npm to pnpm package manager for better performance and disk space efficiency.
        - **Project Documentation & Developer Experience**: Created expansive documentation covering tech stack specifications, setup instructions, build processes, and production deployment guidelines.

### Debugging: Lucky Chicken (Full-Stack Website)

- **Highlights**
    - **Highlights of 2022**
        - **Full-Stack Web Application Architecture**: Quickly grasped the full-stack equipment rental management system with multi-tenant architecture supporting both cooperative (coop) and tenant-specific operations, which has 25+ backend modules and no type support in the codebase.
        - **Logging Implementation**: Added detailed logging for database connection states, server startup, and API request failures to track server health.
        - **Production Environment Analysis**: Isolated root causes by differentiating between production/development environments and database/api request load under pressure.
        - **Improvement Suggestion & Examples:** Provided improvement suggestions by implementing multiple sample api and functionality handling that can sustain under heavy load.
    

### Cleaning: Client Portfolio (WordPress Website)

- **Highlights**
    - **Highlights of 2019**
        - **Website Architecture**: Easily grasped the WordPress Portfolio website architecture and designed a modification plan
        - **Migration to Static Website:** Removed WordPress-related code from the zipped version of the WordPress website to migrate it to a simple static HTML/JS website
        - **Navigation Update:** Dynamically handled tricky navigation without duplicating related code

---

# Others (2022 - Present)

**Contribution Overview:** Served as technical lead for project analysis and proposal estimation while driving company culture improvements through active mentorship and team collaboration. Streamlined operations by automating repetitive processes, contributed to knowledge sharing through regular blog publications, and played a crucial role in recruitment and technical training sessions. Additionally, championed company sports initiatives, fostering team building and workplace engagement across the organization.

### Requirement Analysis & Project Proposal

- **Highlights**
    - **Highlights of 2025**
        - **Customized ERP for Sonar Bangla Hardware:** Designed a cost-efficient solution from a 50+ page requirement document provided by the client
        - **BD Gas Deployment Migration:** Focused on migration to on-premises Windows Server from AWS
        - **HopNGo Online Travel Agency:** R&D and planning for travel itinerary with customizable hotel, air, and car rental system for customers and admin panel
        - **Palli Biddut Somiti (PBS):** Analyze the requirements related to HR, Payroll, and Training of PBS
        - **Smart Job Matching Platform:** Analysis and estimation for MVP project with multi-lingual support
        - **BGFCL School:** Planning and estimation for a complete school management system for Students, HR, Payroll, Accounting, Payment, and so on
    - **Highlights of 2024**
        - **LMS - Nahid’s Batch:** Meeting, analysis, and designing the final proposal with online management of the existing offline coaching platform with attendance device integration, student/guardian/admin management, and exam/marking system
        - **Custom Online Coaching Platform:** Meeting, analysis, and designing the final proposal with granular role-based control for phase-wise implementation of the Australian home-based coaching platform
        - **Freebling Analysis:** Planning and estimation of redesigning and extending the existing web3-focused website with a modern tech stack by following the Figma design
        - **Bangladesh Gas Field:** Meeting, analysis, and designing the final proposal with advanced reporting and setup extension after understanding the existing manual Excel system
    - **Highlights of 2023**
        - **CLS - Learning Management:** Meeting, R&D, and designing the final proposal, including mobile app and website for a complete learning management system with online and offline coaching support
    - **Highlights of 2022**
        - **My Moves Matter:** Estimation of health app with full-stack admin website where user can track his medication schedule, keep journals and so on

### Presentation

- **Highlights**
    - **August 2025:** Review pitch deck for Biddaan
    - **July 2025:** Tech session on [Automation of Daily Workflow](https://github.com/Encryptioner/blogs/blob/master/presentations/Automation%20of%20Daily%20Workflow%20Presentation.md)
    - **July 2025:** Tech session on [Hands-on Coding of Basic Application Tools](https://github.com/Encryptioner/blogs/blob/master/presentations/Hands%20on%20Coding%20of%20Basic%20Application%20Tools.md)
    - **September 2024:** To BD Gas Field officials at Brahmanbaria on `Gas Production Management System - Software Solution and Implementation Proposal`
    - **June 2022:** Tech session on [Tailwind CSS - Modern CSS Framework](https://docs.google.com/presentation/d/1AI80HqqOda2c7xE6h6_qCE8ik9ruGnpXc_kkrmRD2Qs/edit?usp=sharing)
    - **March 2020:** Workshop on React Native for beginners
    - **June 2019:** Starting journey with React

### Automation

- **Highlights**
    - Ensured automated workflow wherever possible
    - Defined notification triggers in Bitbucket, GitHub, Jira, Trello, Jenkins, etc
    - Designed build scripts for Bitbucket, Jenkins, Nginx, AWS, and the Production server
    - Designed IDE setups, AI/MCP integration samples for team productivity boost up
    - Set up power-ups and automation rules for Trello
    - Defined triggers and actions for Jira

### Blog

- **Highlights**
    - Been a regular blog writer for the company website
    - Covered different topics on development, programming, automation, productivity, etc.
    - Check the blogs here: [https://nerddevs.com/author/ankur/](https://nerddevs.com/author/ankur/)

### Recruitement

- **Highlights**
    - Designed written questions and answers for fresher and senior role
    - Curated sample software projects and valuation criteria for candidates
    - Reviewed and marked answer sheets of candidates
    - Be part of final interview board for candidates in Fresher, Senior, UX Designers, App Developer roles
    - Designed comparision table of candidates based multiple stage of recruitment process

### Non-Technical

- **Highlights**
    - Trained interns to follow the best software practices in real-world projects
    - Mentored teammates for career growth and performance boost
    - Arranged and promoted tech sessions inside the company
    - Designed feedback forms to assess team morale
    - Be a key performer in intra-company sports like Cricket, Football etc.
    - Ranked as a top performer at inter-company Cricket competitions

---