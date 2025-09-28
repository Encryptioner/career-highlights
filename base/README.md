# Career Highlights Visualization

Comprehensive python-based system generating professional visualizations across three domains: personal career progression, Nerddevs professional journey, and project portfolio analysis.

## 📁 Directory Structure & Documentation

```
base/
├── README.md                                        # This file - system overview
├── requirements.txt                                 # Python dependencies (matplotlib, pandas, seaborn, numpy)
├── venv/                                            # Python environment
├── Yearwise Personal Highlights/                    # Personal career highlights
│   ├── Yearwise Personal Highlights.md              # Career journey documentation
│   ├── graphical/                                   # Data sources & visualization guides
│   ├── generation/                                  # Python visualization scripts (3 files)
│   └── visual/                                      # → Generated images: timeline, tech mastery, dashboard
├── Yearwise Highlights in ND/                       # Nerddevs professional career
│   ├── Yearwise Highlights in ND.md                 # Professional journey documentation
│   ├── graphical/                                   # Data sources & visualization config
│   ├── generation/                                  # Python visualization scripts (3 files)
│   └── visual/                                      # → Generated images: comprehensive, timeline, tech analysis
├── Projectwise Personal Highlights/                 # Personal project portfolio
│   ├── Projectwise Personal Highlights.md           # Project portfolio documentation
│   ├── graphical/                                   # Data sources & project analysis
│   ├── generation/                                  # Python visualization scripts (3 files)
│   └── visual/                                      # → Generated images: portfolio, innovation, tech evolution
└── Projectwise Highlights in ND/                    # Nerddevs professional projects
    ├── Projectwise Highlights in ND.md              # Professional project documentation
    ├── graphical/                                   # Data sources & project metrics
    ├── generation/                                  # Python visualization scripts (3 files)
    └── visual/                                      # → Generated images: comprehensive, tech evolution, business impact
```

## 🎯 System Overview

**Four Visualization Domains:**
1. **Personal Career** - Career progression, technology mastery, professional growth
2. **Nerddevs Professional** - 7-year journey (2019-2025), role advancement, 200K+ user impact
3. **Personal Projects** - 16+ projects (2016-2025), Java OOP → WebAssembly AI evolution
4. **Nerddevs Projects** - 18+ professional projects, AI/ML innovation, enterprise solutions

**Total Output:** 12 high-quality visualizations (300 DPI) across career timelines, technology evolution, and business impact analysis.

## 🚀 Quick Start

**Prerequisites:** Python 3.8+, virtual environment

**Setup Environment:**
```bash
cd base
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Troubleshooting Installation:**
If you encounter an "externally-managed-environment" error:
```bash
# Remove and recreate virtual environment
rm -rf venv
python3 -m venv venv

# Install using venv Python directly (bypasses environment conflicts)
/path/to/career-highlights/base/venv/bin/python -m pip install -r requirements.txt
```

**Generate All Visualizations:**
```bash
cd base && source venv/bin/activate

# Nerddevs Projects (3 images)
cd "Projectwise Highlights in ND/generation"
python projectwise_nd_comprehensive_dashboard.py && python projectwise_nd_technology_evolution.py && python projectwise_nd_business_impact.py

# Go back to base directory
cd '../..'

# Personal Projects (3 images)
cd "Projectwise Personal Highlights/generation"
python projectwise_comprehensive_dashboard.py && python projectwise_innovation_timeline.py && python projectwise_technology_analysis.py

# Nerddevs Professional (3 images)
cd "Yearwise Highlights in ND/generation"
python nerddevs_comprehensive_dashboard.py && python nerddevs_career_timeline.py && python nerddevs_technology_mastery.py

# Personal Career (3 images)
cd "Yearwise Personal Highlights/generation"
python enhanced_career_timeline.py && python technology_mastery_dashboard.py && python comprehensive_career_dashboard.py
```

**Features:**
- ✅ Relative paths - portable across systems
- ✅ Auto-creates output directories
- ✅ Overrides existing images when re-run
- ✅ 300 DPI publication-quality output

## 📊 Data Sources & Output

**Data:**
- Personal Career: Embedded in Python scripts
- Nerddevs Professional/Projects: JSON files in `graphical/diagram_ready_data.json`
- All data includes visualization config with colors, branding, and styling

**Output:** 12 images total (300 DPI PNG)
- Personal Career: 3 images (timeline, tech mastery, dashboard)
- Nerddevs Professional: 3 images (comprehensive, timeline, tech analysis)
- Personal Projects: 3 images (portfolio, innovation, tech evolution)
- Nerddevs Projects: 3 images (comprehensive, tech evolution, business impact)

## 📝 Technical Notes

**Dependencies:** matplotlib 3.10+, pandas 2.3+, seaborn 0.13+, numpy 2.3+

**Features:**
- Relative paths - portable across systems
- Auto-creates output directories
- Overrides existing images when re-run
- Advanced chart types: timelines, radar charts, bubble charts, heatmaps
- Professional design: gradients, consistent branding, multi-panel layouts

**Performance:** 3-8 seconds per visualization, <150MB memory usage

---

*Career Highlights Visualization - Professional data visualization across multiple domains and timelines.*