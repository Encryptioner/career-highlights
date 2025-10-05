# Projectwise Personal Highlights

Created: August 3, 2025 2:03 PM
Date: December 31, 2025
Tags: Special Entry

**Projectwise Highlights** of [Mir Mursalin Ankur’s](https://encryptioner.github.io/) work outside the regular office

*Last Updated: September 21, 2025*

---

---

# Overall Journey (2016 - 2025)

Throughout my personal development journey, I have consistently embraced challenges and pursued excellence across a wide range of technologies and domains. From academic projects to innovative open-source contributions, and from traditional applications to cutting-edge AI systems, I have consistently chosen tools and approaches that push the boundaries of what's possible while sharing knowledge with the community.

My journey has taken me from foundational programming concepts to pioneering browser-based AI inference, marked by both technical growth and a commitment to open-source development. I have created projects that serve diverse audiences—from educational platforms that help beginners learn modern frameworks to revolutionary tools that eliminate server dependencies for AI processing.

I have architected solutions spanning multiple domains—from traditional board games and cryptographic tools to real-time chat systems and machine learning research—where I've delivered impactful innovations such as WebAssembly-based LLM inference, privacy-first content creation platforms, and comprehensive educational boilerplates that became foundations for learning modern web development.

Beyond individual projects, I've championed accessibility and knowledge sharing through detailed documentation, progressive learning structures, and open-source contributions. I've invested in creating tools that streamline workflows for other developers while fostering innovation through educational content and comprehensive examples.

At the core, my focus has always been on building maintainable, impactful solutions that create real value for users and the developer community—while continuously learning and exploring emerging technologies that shape the future of software development.

### **Programming Languages & Expertise**

- **Systems Programming**: C, C++ (Shell implementation, OpenGL graphics, Assembly)
- **Web Development**: JavaScript/TypeScript, PHP, Python (Django, Laravel, Node.js)
- **Machine Learning**: Python (TensorFlow, Keras, scikit-learn, OpenCV)
- **Mobile & Desktop**: Java, Dart/Flutter
- **Database Technologies**: PostgreSQL, MongoDB, Redis

### **Framework & Technology Proficiency**

- **Frontend**: React, Vue.js, HTML5/CSS3, Tailwind CSS, shadcn/ui
- **Backend**: NestJS, Django, Laravel, Node.js/Koa, Express
- **DevOps**: Docker, GitHub Actions, CI/CD pipelines
- **Testing**: Jest, PHPUnit, Playwright, Newman/Postman, Locust
- **Cloud & Deployment**: GitHub Pages, Heroku, Render, Vercel

### **Project Complexity Spectrum**

- **Research Level**: Machine learning thesis with multi-dataset validation
- **Enterprise Level**: Full-stack monorepo with authentication and microservices
- **Systems Level**: Unix shell implementation with cross-platform support
- **Educational Level**: Structured learning platforms with progressive complexity

### **Development Practices**

- **Code Quality**: Automated linting, pre-commit hooks, comprehensive testing
- **Documentation**: API documentation, technical writing, README creation
- **Version Control**: Git workflows, branching strategies, commit message standards
- **Architecture**: Modular design, separation of concerns, scalable patterns

---

# Local Whisper: Private Chat (2025)

**Project Overview:** In the Nerddevs hackathon, developed a good-looking browser-based AI chat assistant that runs Large Language Models entirely in the browser using WebAssembly. Successfully created a privacy-focused, offline-capable AI system with plug-and-play embed functionality for seamless website integration.

- **Key Tools**
    - **Core Stack**: React 18, Vite 5.4, TypeScript, WebAssembly
    - **AI Engine**: @wllama/wllama 2.3.4 for local LLM inference
    - **UI Framework**: Radix UI themes 3.1, Heroicons React 2.2
    - **Model Format**: GGUF models from Hugging Face (SmolLM2, Llama 3.2)
    - **Content Processing**: react-markdown, react-syntax-highlighter
    - **Development**: ESLint 9, Prettier 3, concurrent development scripts
    - **Deployment**: GitHub Actions, automatic model downloading
- **References**
    - **Public Website:** [https://encryptioner.github.io/private-chat/](https://encryptioner.github.io/private-chat/)
    - **Github:** [https://github.com/Encryptioner/private-chat](https://github.com/Encryptioner/private-chat)

### Public (Static Website with Framework)

- **Highlights**
    - **Highlights of 2025**
        - **Revolutionary Browser AI**: Pioneered running complete Large Language Models (SmolLM2, Llama 3.2) entirely in the browser using WebAssembly, eliminating server dependencies and ensuring complete privacy with chat history
        - **Plug-and-Play Embed System**: Created seamless integration solution with single script tag implementation, automatically providing floating chat widget or custom div placement for any website
        - **Advanced Model Management**: Built sophisticated system supporting multiple GGUF model formats with automatic caching, offline functionality, and custom model upload capabilities (up to 2GB)
        - **WebAssembly Optimization**: Implemented high-performance inference engine using Wllama with proper CORS headers, memory management, and context window optimization for efficient chat conversations
        - **Zero-Backend Architecture**: Achieved complete client-side AI processing with speech synthesis integration, responsive design, and production-ready deployment pipeline for maximum accessibility

---

# Markdown to Slide (2025)

**Project Overview:** Developed a modern browser-based presentation platform that transforms Markdown content into professional slide decks. Successfully delivered a comprehensive presentation tool with real-time editing, PDF export capabilities, and PWA functionality for seamless offline use.

- **Key Tools**
    - **Core Stack**: Next.js 15, React 19, TypeScript 5, Node.js 18+
    - **Build System**: Vite with Turbopack, pnpm package management
    - **Styling**: TailwindCSS 4 with custom design tokens
    - **Markdown Processing**: marked.js with DOMPurify sanitization
    - **PDF Generation**: pdfmake for client-side PDF export
    - **Development**: ESLint 9, Prettier, Jest testing framework
    - **Deployment**: GitHub Actions with static export for GitHub Pages
- **References**
    - **Public Website:** [https://encryptioner.github.io/markdown-to-slide/](https://encryptioner.github.io/markdown-to-slide/)
    - **Github:** [https://github.com/Encryptioner/markdown-to-slide](https://github.com/Encryptioner/markdown-to-slide)

### Public (Static Website with Framework)

- **Highlights**
    - **Highlights of 2025**
        - **Real-time Markdown Editor**: Built comprehensive presentation creation system with live preview, slide separation using `--`, and support for custom backgrounds (colors, images, videos)
        - **Professional PDF Export**: Implemented client-side PDF generation with pdfmake, preserving formatting and custom slide attributes for high-quality presentation downloads
        - **PWA Capabilities**: Developed Progressive Web App functionality with service worker, offline support, and installation capabilities across desktop and mobile platforms
        - **AI Chat Integration**: Integrated embeddable AI assistant with local LLM processing for presentation help and suggestions, completely privacy-focused with no server communication
        - **Advanced Slide Features**: Created a sophisticated slide attribute system supporting custom backgrounds, responsive design, keyboard navigation, and full-screen presentation mode

---

# LinkedInify (2025)

**Project Overview:** Created a privacy-first Progressive Web App that converts Markdown content into LinkedIn-ready posts. It also provides a rich text editor for easy co-editing and content creation. Built with modern modular JavaScript architecture, delivering a comprehensive social media content creation tool with offline capabilities and AI-powered features.

- **Key Tools**
    - **Core Stack**: Vanilla JavaScript ES6+, Vite 4.5, pnpm 8.15
    - **Build System**: Vite with PWA plugin, Workbox for service worker
    - **Styling**: Modern CSS with custom properties, responsive design
    - **Markdown Processing**: marked.js 9.1 for content conversion
    - **Testing**: Vitest with coverage, jsdom environment
    - **Development**: ESLint 8, Prettier 3, Husky git hooks
    - **Deployment**: GitHub Actions, GitHub Pages, and static hosting are compatible
- **References**
    - **Public Website:** [https://encryptioner.github.io/linkedinify](https://encryptioner.github.io/linkedinify)
    - **Github:** [https://github.com/Encryptioner/linkedinify](https://github.com/Encryptioner/linkedinify)

### Public (Static Website with Framework)

- **Highlights**
    - **Highlights of 2025**
        - **Privacy-First Architecture**: Developed complete offline functionality with no server communication, all data processing happens locally with localStorage persistence and 100% privacy protection
        - **Modular JavaScript System**: Built sophisticated ES6 modular architecture with EventEmitter-based inter-module communication, including ThemeManager, ContentConverter, HistoryManager, and TitleGenerator modules
        - **AI-Powered Content Generation**: Implemented multi-language AI title generation system with pattern recognition for business, technical, and personal content categories
        - **Professional LinkedIn Preview**: Created real-time preview system supporting both light/dark modes and desktop/mobile layouts, accurately reflecting LinkedIn's actual appearance
        - **PWA Excellence**: Achieved comprehensive Progressive Web App implementation with service worker caching, offline functionality, mobile installation, and desktop app capabilities

---

# Service Charge Bill Calculator (2025)

**Project Overview:** Developed a modern web application for creating and managing service charge bills for apartment buildings. Successfully delivered a comprehensive billing solution with multi-language support, flexible billing options, professional PDF export, and PWA functionality for offline use with auto-save capabilities.

- **Key Tools**
    - **Core Stack**: Astro 5, React 19, TypeScript 5, Node.js 22
    - **Build System**: Vite with pnpm package management
    - **Styling**: Tailwind CSS 4 with custom design tokens
    - **UI Components**: React with TypeScript integration
    - **PDF Generation**: jsPDF with html2canvas for professional bill export
    - **Internationalization**: Multi-language support (English, Bangla)
    - **PWA Features**: Service worker, offline functionality, manifest
    - **Deployment**: GitHub Actions with dual deployment modes (GitHub Pages/Custom Domain)
- **References**
    - **Public Website:** [https://encryptioner.github.io/service-charge/](https://encryptioner.github.io/service-charge/)
    - **Github:** [https://github.com/Encryptioner/service-charge](https://github.com/Encryptioner/service-charge)

### Public (Static Website with Framework)

- **Highlights**
    - **Highlights of 2025**
        - **Multi-Category Billing System**: Built comprehensive service charge calculator supporting unlimited categories with flexible billing types (single flat or divided across all flats)
        - **Multi-Language Architecture**: Implemented modular internationalization system with English and Bangla support, easily extensible to additional languages through configuration
        - **Professional PDF Export**: Developed sophisticated PDF generation handling Tailwind CSS v4 OKLCH color conversion to RGB for accurate rendering with print functionality
        - **PWA Excellence**: Created Progressive Web App with service worker caching, offline functionality, and auto-save using localStorage for data persistence
        - **Privacy-First Design**: Achieved complete client-side processing with no server communication, ensuring all billing data stays private in the user's browser

---

# Fish & Boat Ladder Game (2025)

**Project Overview:** Developed a modern, browser-based variant of the classic Snakes and Ladders board game (Ludo), featuring fish and boats instead of traditional elements. Successfully created a comprehensive two-player game with PWA capabilities, offline functionality, and mobile-optimized responsive design.

- **Key Tools**
    - **Core Stack**: Vanilla HTML5, CSS3, JavaScript ES6+ (no external dependencies)
    - **Game Architecture**: Class-based design with FishBoatLaddersGame main class
    - **Styling**: CSS Grid layout, CSS custom properties, responsive design
    - **Audio System**: Web Audio API for synthesized sound effects
    - **PWA Features**: Service worker caching, web app manifest
    - **State Management**: localStorage with JSON persistence and error handling
    - **Development**: Live Server for development, no build process required
- **References**
    - **Public Website:** [https://encryptioner.github.io/fish-boat-ludu/](https://encryptioner.github.io/fish-boat-ludu/)
    - **Github:** [https://github.com/Encryptioner/fish-boat-ludu](https://github.com/Encryptioner/fish-boat-ludu)

### Public (Static Website)

- **Highlights**
    - **Highlights of 2025**
        - **Innovative Game Mechanics**: Reimagined classic Snakes and Ladders with a nautical theme using fish (🦈) to drag players down and boats (🚢⛵) to lift players, creating engaging visual storytelling
        - **PWA Excellence with Offline Support**: Built comprehensive Progressive Web App with service worker caching, enabling complete offline gameplay after initial load and mobile app installation capabilities
        - **Advanced Game State Management**: Implemented a sophisticated persistence system with localStorage, tracking player statistics, move history with timestamps, and editable player names across browser sessions
        - **Mobile-First Responsive Design**: Created touch-optimized interface with hamburger menu, no-scroll mobile layout, and webview compatibility for seamless mobile app integration
        - **Professional Audio-Visual Experience**: Developed a complete sound system using Web Audio API with dice rolling, fish bites, boat rescues, and victory sounds, plus smart animations for enhanced user engagement
        

---

# CCSH Shell (2025)

**Project Overview:** Architected and implemented a comprehensive Unix-like shell from scratch in C, featuring advanced command-line functionality and cross-platform compatibility. Designed with emphasis on portability, user experience, and modern shell features, including job control and command aliasing.

- **Key Tools**
    - **Core Language**: C with POSIX compliance
    - **Libraries**: GNU Readline for enhanced command-line experience
    - **Build System**: GNU Makefile with cross-platform support
    - **Platforms**: Linux, macOS, BSD variants with automated testing
    - **Development**: Signal handling, process management, memory management
- **References**
    - **Github:** [https://github.com/Encryptioner/ccsh-shell](https://github.com/Encryptioner/ccsh-shell)

### Code & Blog & Presentation

- **Highlights**
    - **Highlights of 2025**
        - **Advanced Shell Implementation**: Developed fully-functional Unix shell with comprehensive feature set, including interactive command line, job control for background/foreground processes, and robust signal handling mechanisms
        - **Cross-Platform Compatibility**: Engineered portable shell implementation supporting Linux, macOS, and BSD variants with an automated build and packaging system for seamless deployment across different Unix-like systems
        - **Modern Command-Line Features**: Integrated GNU Readline support for command history, tab completion, and command editing, along with advanced features like input/output redirection, pipelines, and command aliases
        - **Production-Ready Architecture**: Implemented comprehensive error handling, memory management, and process control with emphasis on reliability and performance for daily command-line usage

---

# De-Encrypt Hub (2025)

**Project Overview:** Developed a comprehensive browser-based encryption and decryption toolkit using modern React and TypeScript architecture. Successfully delivered a feature-rich cryptographic platform with educational components and an intuitive user interface design.

- **Key Tools**
    - **Core Stack**: React 18, TypeScript 5.5, Vite 5.4, Node.js 22
    - **UI Framework**: shadcn/ui components with Radix UI primitives
    - **Styling**: Tailwind CSS 3.4 with custom theme support
    - **Cryptography**: Web Crypto API, CryptoJS, jose library
    - **State Management**: React hooks with custom crypto-specific hooks
    - **Build System**: Vite with SWC, pnpm package management
    - **Development**: ESLint 9.9, GitHub workflows for CI/CD
- **References**
    - **Public Website:** [https://encryptioner.github.io/de-encrypt-hub/](https://encryptioner.github.io/de-encrypt-hub/)
    - **Github:** [https://github.com/Encryptioner/de-encrypt-hub](https://github.com/Encryptioner/de-encrypt-hub)

### Public (Static Website with Framework)

- **Highlights**
    - **Highlights of 2025**
        - **Complete Cryptographic Foundation**: Built an entire encryption platform from scratch with React/Vite stack, implementing comprehensive cipher support including AES, DES, TripleDES, Rabbit, and RC4 algorithms
        - **Advanced UI/UX Architecture**: Designed sophisticated tabbed interface with encrypt/decrypt modes, file upload capabilities, and mobile-responsive design using shadcn/ui components
        - **Educational Visualization System**: Created a step-by-step animation system for cryptographic processes, making complex algorithms accessible through interactive visualizations and detailed explanations
        - **Multi-Format Encryption Support**: Implemented image encryption/decryption, PDF processing, and file-based encryption with download functionality across all supported formats
        - **Professional Development Workflow**: Established comprehensive development environment with documentation, GitHub workflows, and pnpm migration for enhanced developer experience

---

# Laravel Learning Platform (2025)

**Project Overview:** Developed a comprehensive Laravel example application designed as an educational resource for beginners. Created progressive learning experience with commit-by-commit structure, integrating modern full-stack development practices, including Vue.js frontend and comprehensive testing framework.

- **Key Tools**
    - **Backend**: Laravel framework with PHP (41%)
    - **Frontend**: Vue.js (39.1%), Blade templating (18.4%)
    - **Styling**: Tailwind CSS for modern UI design
    - **Build System**: Vite for fast development and building
    - **Testing**: PHPUnit for comprehensive test coverage
    - **Languages**: TypeScript and JavaScript for frontend logic
- **References**
    - **Github:** [https://github.com/Encryptioner/laravel-example-app](https://github.com/Encryptioner/laravel-example-app)

### Public (Static Website with Framework)

- **Highlights**
    - **Highlights of 2025**
        - **Progressive Learning Structure**: Designed educational Laravel application with an incremental commit-by-commit learning approach, enabling beginners to understand modern PHP web development through structured progression
        - **Modern Full-Stack Integration**: Implemented comprehensive Laravel application with Vue.js frontend integration, Tailwind CSS styling, and Vite build system, representing current industry best practices
        - **Production-Ready Development**: Established complete development workflow with PHPUnit testing framework, modern JavaScript tooling, and comprehensive documentation for an effective learning experience

---

# Django Learning Platform (2025)

**Project Overview:** Built a modern Django example application using the latest Django 5.1 framework, emphasizing code quality, best practices, and structured learning approach. Implemented comprehensive development workflow with automated code quality tools and multi-module architecture.

- **Key Tools**
    - **Framework**: Django 5.1 (latest version)
    - **Languages**: Python (81.6%), HTML (15.6%), CSS (2.8%)
    - **Code Quality**: flake8, pylint, pre-commit hooks
    - **Architecture**: Multi-app structure (polls, blog modules)
    - **Development**: Structured learning through branches and commits
- **References**
    - **Github:**  [https://github.com/Encryptioner/django-example-app](https://github.com/Encryptioner/django-example-app)

### Public (Static Website with Framework)

- **Highlights**
    - **Highlights of 2025**
        - **Latest Django Implementation**: Developed comprehensive Django 5.1 application showcasing modern Python web development practices with emphasis on clean code architecture and maintainable project structure
        - **Code Quality Excellence**: Integrated automated code quality tools, including flake8, pylint, and pre-commit hooks, ensuring consistent code standards and best practices throughout the development lifecycle
        - **Educational Framework Design**: Created a structured learning experience through organized commits and branches with multiple app modules (polls, blog), demonstrating scalable Django application architecture
        - **Modern Development Practices**: Implemented contemporary Python web development workflow with emphasis on testing, code quality, and comprehensive documentation for effective skill development

---

# Personal Portfolio Website (2024)

**Project Overview:** Developed and maintained a professional portfolio website showcasing technical projects and professional experience. Implemented responsive web design principles with theme switching and deployed using GitHub Pages for optimal accessibility and performance.

- **Key Tools**
    - **Frontend**: HTML5, CSS3, ReactJS, Typescript, Chakra UI
    - **Deployment**: GitHub Pages with automated CI/CD
    - **Design**: Responsive web design principles
    - **Assets Management**: Optimized images and multimedia content
- **References**
    - **Public Website:** [https://encryptioner.github.io/](https://encryptioner.github.io/)

### Public (Static Website with Framework)

- **Highlights**
    - **Highlights of 2024**
        - **Professional Web Presence**: Designed and developed comprehensive personal portfolio website featuring project showcases, technical skills, and professional experience with a clean, responsive design
        - **GitHub Pages Integration**: Implemented automated deployment pipeline using GitHub Pages with continuous integration for seamless content updates and version control
        - **Responsive Design Implementation**: Created a mobile-first responsive website, ensuring optimal viewing experience across all device types and screen sizes
        - **Performance Optimization**: Optimized website assets, images, and multimedia content for fast loading times and excellent user experience

---

# Frontend Vue3 Boilerplate (2022)

**Project Overview:** Created a production-ready Vue.js 3 boilerplate with modern development tooling and comprehensive testing frameworks. Established an enterprise-grade template for rapid Vue application development.

- **Key Tools**
    - **Core Stack**: Vue.js 3.2, TypeScript 4.7, Vite 2.9, Node.js 16
    - **State Management**: Pinia 2.0 with persisted state plugin
    - **UI Framework**: Tailwind CSS 3.1, DaisyUI, Heroicons
    - **Testing**: Vitest for unit tests, Playwright for E2E testing
    - **Build System**: Vite with hot module replacement
    - **Code Quality**: ESLint with Airbnb configuration
    - **Deployment**: GitHub Pages with automated workflows
- **References**
    - **Public Website:** [https://encryptioner.github.io/frontend-vue3-boilerplate/](https://encryptioner.github.io/frontend-vue3-boilerplate/)
    - **Github:** [https://github.com/Encryptioner/frontend-vue3-boilerplate](https://github.com/Encryptioner/frontend-vue3-boilerplate)

### Public (Static Website with Framework)

- **Highlights**
    - **Highlights of 2022**
        - **Modern Vue 3 Foundation**: Established complete Vue 3 boilerplate using the latest Composition API patterns, TypeScript integration, and Pinia state management with persistence capabilities
        - **Comprehensive Development Tooling**: Implemented auto-import systems for components and composables, TypeScript checker integration with Vite, and custom font loading with Tailwind CSS
        - **Advanced UI Component System**: Built sophisticated navigation system with mobile responsiveness, theme switching capabilities, and ecommerce-style filtering components with Heroicons integration
        - **Production Deployment Pipeline**: Configured automated GitHub Pages deployment with environment-based configurations, supporting both development and production build processes
        - **Code Quality & Testing Infrastructure**: Established ESLint configuration with Tailwind CSS plugin, removed Prettier conflicts, and implemented comprehensive testing strategy for reliable production deployments
    

---

# NestJS VueJS TypeScript Boilerplate (2022)

**Project Overview:** Architected a comprehensive full-stack TypeScript monorepo demo website combining an enterprise-grade NestJS backend with Vue.js frontend and deployed a production-ready application template with complete authentication, database integration, and deployment strategies.

- **Key Tools**
    - **Core Stack**: Node.js 16, TypeScript 4.5, Yarn workspaces
    - **Backend Framework**: NestJS 8.2, Express 4.17
    - **Frontend Framework**: Vue.js 2.6, Vuetify 2.2
    - **Database**: MongoDB 5.0 with Mongoose 6.0
    - **Authentication**: Passport.js, JWT, OAuth (Google/Facebook)
    - **Infrastructure**: Redis caching, BullMQ queues, Winston logging
    - **DevOps**: Docker containerization, Heroku deployment
- **References**
    - **Public Website:** [https://typescript-boilerplate-0.herokuapp.com/](https://typescript-boilerplate-0.herokuapp.com/)

### Public (Full-Stack Website)

- **Highlights**
    - **Highlights of 2022**
        - **Complete Monorepo Architecture**: Established full-stack TypeScript boilerplate with 5-workspace structure (client, server, utilities, types, dto), enabling shared type definitions across the entire application stack
        - **Enterprise Authentication System**: Built comprehensive authentication module with JWT tokens, OAuth integration for Google and Facebook, role-based access control, and secure API endpoint protection
        - **Production Infrastructure Setup**: Implemented complete backend infrastructure with MongoDB integration, Redis caching, email services via Mailgun, file upload handling, and comprehensive logging system with Winston
        - **Heroku Deployment Pipeline**: Configured production deployment strategy with Docker containerization, environment variable management, and automated deployment scripts for seamless cloud hosting
        - **API Documentation & Testing**: Integrated Swagger documentation with authorized endpoints, comprehensive DTO validation, and API testing framework for reliable backend service development
        - **Cloud Deployment Expansion**: Added Render deployment scripts, expanding deployment options beyond Heroku for increased platform flexibility and hosting alternatives
    

---

# Text-Bomb Chat Application (2019)

**Project Overview:** Developed a real-time web chat application using Django and modern web technologies, featuring user authentication, real-time messaging, and background task processing. Implemented comprehensive user management system with email notifications and profile features.

- **Key Tools**
    - **Backend**: Django framework with Python
    - **Real-time**: WebSocket integration for live chat
    - **Task Processing**: Redis and Celery for background jobs
    - **Frontend**: HTML, CSS, JavaScript for interactive UI
    - **Email**: Google SMTP integration for notifications
    - **Database**: Django ORM with PostgreSQL/SQLite support
- **References**
    - **Github:** [https://github.com/Encryptioner/Text-Bomb](https://github.com/Encryptioner/Text-Bomb)

### Public (Full-Stack Website)

- **Highlights**
    - **Highlights of 2019**
        - **Real-Time Chat System**: Built comprehensive web chat application with real-time messaging capabilities using WebSocket technology and Django Channels for seamless user communication experience
        - **User Management Infrastructure**: Implemented complete user registration system with email verification, profile management, and authentication using Django's built-in security features
        - **Background Task Processing**: Integrated Redis and Celery for asynchronous task handling, including hourly notifications and email processing, ensuring optimal application performance
        - **Production-Ready Deployment**: Configured Google SMTP integration for reliable email notifications and implemented scalable architecture supporting concurrent users
    

---

# Thesis - Facial Expression Recognition (2018)

**Project Overview:** Conducted advanced machine learning research project for graduation thesis, implementing a comprehensive facial expression recognition system using multiple state-of-the-art approaches. Successfully developed and compared three different methodologies (LBP, CNN, SVM) across four major datasets, demonstrating a deep understanding of computer vision and machine learning algorithms.

- **Key Tools**
    - **Core Stack**: Python 3.5, TensorFlow, Keras, scikit-learn
    - **Computer Vision**: OpenCV for image processing and facial landmark detection
    - **Machine Learning**: Support Vector Machine (SVM), Convolutional Neural Networks (CNN)
    - **Feature Extraction**: Local Binary Patterns (LBP) with rotational invariant implementation
    - **Data Processing**: NumPy, pandas for data manipulation and analysis
    - **Datasets**: CK+, JAFFE, KDEF, FER2013 emotion recognition datasets
    - **Academic Tools**: Jupyter Notebook for research documentation and analysis
- **References**
    - **Github:** [https://github.com/Encryptioner/Thesis-FER-based-on-LBP-CNN-on-SVM](https://github.com/Encryptioner/Thesis-FER-based-on-LBP-CNN-on-SVM)

### Code & Presentation

- **Highlights**
    - **Highlights of 2018**
        - **Advanced ML Research Implementation**: Developed comprehensive facial expression recognition system using three distinct approaches - Local Binary Patterns with 24-point 8-radius rotational invariant features, deep Convolutional Neural Networks, and Support Vector Machine classification
        - **Multi-Dataset Validation**: Conducted extensive experimental validation across four major emotion recognition datasets (CK+, JAFFE, KDEF, FER2013) ensuring robustness and generalizability of the proposed methodology
        - **68-Point Facial Landmark System**: Implemented sophisticated facial landmark detection system for precise feature extraction and alignment, enabling accurate emotion classification across 7 different emotional states
        - **Comparative Analysis Framework**: Designed comprehensive evaluation framework comparing performance metrics across different methodologies, providing valuable insights for the facial expression recognition research community
    

---

# OpenGL Car Game (2018)

**Project Overview:** Created an interactive 2D car game using OpenGL and C++, demonstrating computer graphics programming skills and game development fundamentals. Implemented comprehensive game mechanics, including rendering, movement, and user input handling for an engaging gaming experience.

- **Key Tools**
    - **Graphics**: OpenGL for 2D rendering and animation
    - **Programming**: C++ with modular code architecture
    - **IDE**: Code::Blocks for development environment
    - **Game Components**: Separate modules for drawing, movement, keyboard input
    - **Academic Context**: CSE 4202 Computer Graphics course
- **References**
    - **Github:** [https://github.com/Encryptioner/car-game](https://github.com/Encryptioner/car-game)

### Code & Presentation

- **Highlights**
    - **Highlights of 2018**
        - **OpenGL Graphics Implementation**: Developed comprehensive 2D car game using the OpenGL graphics library, demonstrating advanced understanding of computer graphics principles, including rendering, animation, and visual effects
        - **Modular Game Architecture**: Designed a well-structured codebase with separate modules for game mechanics (main.cpp, draw.cpp, move.cpp, keyboard.cpp), ensuring maintainable and extensible game development practices
        - **Interactive Game Mechanics**: Implemented complete game functionality, including player input handling, collision detection, movement physics, and real-time rendering for an engaging gameplay experience

---

# E-Examination System (2017)

**Project Overview:** Designed and developed a comprehensive online examination platform from scratch using PHP and PostgreSQL. Created a full-featured web application with user management, administrative controls, and advanced ranking systems, demonstrating proficiency in full-stack web development and database design.

- **Key Tools**
    - **Backend**: PHP (66.2%), PL/pgSQL stored procedures (25%)
    - **Database**: PostgreSQL with advanced query optimization
    - **Frontend**: HTML, CSS (8.8%), JavaScript for dynamic interactions
    - **Architecture**: MVC pattern with database-driven design
    - **Academic Context**: CSE 3100 course project supervision
- **References**
    - **Github:** [https://github.com/Encryptioner/E-Examination](https://github.com/Encryptioner/E-Examination)

### Public & Admin (Full-Stack Website)

- **Highlights**
    - **Highlights of 2017**
        - **Complete Examination Platform**: Built full-featured online examination system with comprehensive user profile management, secure authentication, and role-based access control for students and administrators
        - **Advanced Ranking System**: Implemented sophisticated ranking and scoring algorithms with real-time leaderboard functionality, providing competitive examination environment for academic assessments
        - **Database-Driven Architecture**: Designed robust PostgreSQL database schema with stored procedures and optimized queries, ensuring data integrity and performance for concurrent examination sessions
        - **Administrative Control Panel**: Developed comprehensive admin interface for examination creation, user management, result analysis, and system configuration, enabling complete platform administration
    

---

# BaghBondi Traditional Game (2016)

**Project Overview:** Developed a Java-based implementation of the traditional Bengali game "BaghBondi" as an academic project, demonstrating object-oriented programming principles and game development concepts. Created an engaging digital version of the classical board game with proper game mechanics and a user interface.

- **Key Tools**
    - **Programming Language**: Java with object-oriented design
    - **Game Development**: Core Java game mechanics and logic
    - **Academic Context**: CSE 2100 course project at RUET
    - **Design Patterns**: Implementation of game design patterns
- **References**
    - **Github:** [https://github.com/Encryptioner/BaghBondi-Game](https://github.com/Encryptioner/BaghBondi-Game)

### Code & Presentation

- **Highlights**
    - **Highlights of 2016**
        - **Traditional Game Digitization**: Successfully translated traditional Bengali board game "BaghBondi" into a digital format using Java, preserving authentic game rules and mechanics while creating an engaging user experience
        - **Object-Oriented Game Architecture**: Implemented comprehensive game structure using Java OOP principles, including inheritance, polymorphism, and encapsulation for a maintainable and extensible codebase
        - **Academic Excellence**: Completed as part of CSE 2100 coursework, demonstrating strong programming fundamentals and ability to deliver complex projects within academic constraints

---