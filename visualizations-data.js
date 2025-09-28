// Career Highlights Visualization Data
const visualizationsData = {
  categories: {
    timeline: {
      name: "Timeline & Growth",
      icon: "📈",
      description: "Career progression and growth stories"
    },
    technology: {
      name: "Technology Mastery",
      icon: "⚡",
      description: "Technical skills and stack evolution"
    },
    business: {
      name: "Business Impact",
      icon: "🎯",
      description: "Quantified results and user metrics"
    },
    projects: {
      name: "Project Portfolio",
      icon: "🚀",
      description: "Innovation and project achievements"
    }
  },

  visualizations: [
    // Personal Career Highlights
    {
      id: "comprehensive_career_dashboard",
      title: "Comprehensive Career Dashboard",
      category: "timeline",
      domain: "personal",
      file: "comprehensive_career_dashboard.png",
      description: "Complete career journey with timeline, technology evolution, and impact metrics",
      metrics: ["9+ Years Experience", "16+ Personal Projects", "Technology Evolution"],
      featured: true
    },
    {
      id: "enhanced_career_timeline",
      title: "Enhanced Career Timeline",
      category: "timeline",
      domain: "personal",
      file: "enhanced_career_timeline.png",
      description: "Detailed career progression with projects, complexity, and innovation milestones",
      metrics: ["Career Growth", "Project Complexity", "Innovation Milestones"]
    },
    {
      id: "technology_mastery_dashboard",
      title: "Technology Mastery Dashboard",
      category: "technology",
      domain: "personal",
      file: "technology_mastery_dashboard.png",
      description: "Skills radar and technology proficiency across different domains",
      metrics: ["15+ Technologies", "Full-Stack Expertise", "AI/ML Integration"]
    },

    // Nerddevs Professional Career
    {
      id: "nerddevs_comprehensive_dashboard",
      title: "Nerddevs Professional Journey",
      category: "timeline",
      domain: "professional",
      file: "nerddevs_comprehensive_dashboard.png",
      description: "7-year professional career at Nerddevs with role progression and achievements",
      metrics: ["7 Years", "Lead Engineer", "200K+ Users Served"],
      featured: true
    },
    {
      id: "nerddevs_career_timeline",
      title: "Professional Career Timeline",
      category: "timeline",
      domain: "professional",
      file: "nerddevs_career_timeline.png",
      description: "Detailed timeline of professional growth, projects, and responsibilities",
      metrics: ["Software → Senior → Lead", "Project Complexity Growth", "Team Leadership"]
    },
    {
      id: "nerddevs_technology_mastery",
      title: "Professional Technology Mastery",
      category: "technology",
      domain: "professional",
      file: "nerddevs_technology_mastery.png",
      description: "Technology stack evolution and expertise in professional environment",
      metrics: ["Vue.js 3", "TypeScript", "Node.js", "AI Integration"]
    },

    // Personal Projects Portfolio
    {
      id: "projectwise_comprehensive_dashboard",
      title: "Personal Projects Portfolio",
      category: "projects",
      domain: "personal-projects",
      file: "projectwise_comprehensive_dashboard.png",
      description: "Complete overview of 16+ personal projects spanning 2016-2025",
      metrics: ["16+ Projects", "9 Years", "Java → WebAssembly Evolution"],
      featured: true
    },
    {
      id: "projectwise_innovation_timeline",
      title: "Innovation Timeline",
      category: "timeline",
      domain: "personal-projects",
      file: "projectwise_innovation_timeline.png",
      description: "Timeline of personal project innovations and technological breakthroughs",
      metrics: ["2016-2025", "Technology Evolution", "Innovation Milestones"]
    },
    {
      id: "projectwise_technology_analysis",
      title: "Personal Projects Technology Analysis",
      category: "technology",
      domain: "personal-projects",
      file: "projectwise_technology_analysis.png",
      description: "Technology distribution and evolution across personal projects",
      metrics: ["15+ Technologies", "Web → AI Evolution", "Cross-Platform"]
    },

    // Nerddevs Projects
    {
      id: "projectwise_nd_comprehensive_dashboard",
      title: "Nerddevs Projects Overview",
      category: "projects",
      domain: "professional-projects",
      file: "projectwise_nd_comprehensive_dashboard.png",
      description: "18+ professional projects with technology distribution and business impact",
      metrics: ["18+ Projects", "Enterprise Solutions", "AI/ML Integration"],
      featured: true
    },
    {
      id: "projectwise_nd_technology_evolution",
      title: "Professional Technology Evolution",
      category: "technology",
      domain: "professional-projects",
      file: "projectwise_nd_technology_evolution.png",
      description: "Technology stack evolution across professional projects",
      metrics: ["Vue.js Expertise", "TypeScript", "Full-Stack Solutions"]
    },
    {
      id: "projectwise_nd_business_impact",
      title: "Business Impact Analysis",
      category: "business",
      domain: "professional-projects",
      file: "projectwise_nd_business_impact.png",
      description: "Quantified business impact and user metrics across professional projects",
      metrics: ["200K+ Users", "Multiple Platforms", "Revenue Impact"]
    }
  ],

  domains: {
    personal: {
      name: "Personal Career",
      color: "#4ECDC4",
      description: "Individual career progression and growth"
    },
    professional: {
      name: "Nerddevs Professional",
      color: "#45B7D1",
      description: "7-year professional journey (2019-2025)"
    },
    "personal-projects": {
      name: "Personal Projects",
      color: "#96CEB4",
      description: "16+ projects spanning 2016-2025"
    },
    "professional-projects": {
      name: "Nerddevs Projects",
      color: "#FF9F43",
      description: "18+ professional projects and solutions"
    }
  }
};

// Export for use in components
if (typeof module !== 'undefined' && module.exports) {
  module.exports = visualizationsData;
}