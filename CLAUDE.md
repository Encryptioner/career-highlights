# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A dual-component career highlights system combining matplotlib-based visualization generation with an interactive web gallery.

**Architecture:**
- `base/` - Python visualization generation system (matplotlib, pandas, seaborn)
- Root directory - Interactive web gallery (vanilla JS, responsive design)

## Key Components

### Visualization Generation (`base/`)
Python-based system generating 12 professional visualizations across 4 career domains:

**Directory Structure:**
- `Yearwise Personal Highlights/generation/` - Personal career visualizations (3 scripts)
- `Yearwise Highlights in ND/generation/` - Professional career visualizations (3 scripts)
- `Projectwise Personal Highlights/generation/` - Personal projects visualizations (3 scripts)
- `Projectwise Highlights in ND/generation/` - Professional projects visualizations (3 scripts)

**Key Scripts:**
- `enhanced_career_timeline.py`, `technology_mastery_dashboard.py`, `comprehensive_career_dashboard.py` - Personal career
- `nerddevs_comprehensive_dashboard.py`, `nerddevs_career_timeline.py`, `nerddevs_technology_mastery.py` - Professional
- `projectwise_*` variations for project portfolios

**Environment:**
- Python 3.8+ with virtual environment at `base/venv/`
- Dependencies: matplotlib 3.10+, pandas 2.3+, seaborn 0.13+, numpy 2.3+

### Web Gallery (Root)
Interactive visualization gallery built with vanilla JavaScript:

**Core Files:**
- `index.html` - Main gallery page
- `components/HighlightsGallery.js` - Main gallery component (425 lines)
- `config/career-highlights-config.json` - Gallery configuration and metadata
- `sw.js` - Service worker for offline support

**Features:**
- Domain-based filtering (Personal, Professional, Projects)
- Category filtering (Timeline, Technology, Business, Projects)
- Lightbox gallery with keyboard/touch navigation
- Responsive design with mobile optimization
- Progressive Web App capabilities

## Common Development Commands

### Generate All Visualizations
- Check Readme in `base` directory

### Serve Web Gallery
```bash
# From root directory
python3 -m http.server 8080
# Access at http://localhost:8080
```

### Optimize Gallery
```bash
node optimize.js  # Validates configuration and optimizes assets
```

## Data Architecture

**Visualization Data Sources:**
- Personal career: Embedded in Python scripts
- Professional/Projects: JSON files in `graphical/diagram_ready_data.json` subdirectories
- Gallery metadata: `config/career-highlights-config.json`

**Output:** 12 high-quality PNG images (300 DPI) in corresponding `visual/` subdirectories

## Configuration Management

**Gallery Config (`config/career-highlights-config.json`):**
- `visualizations[]` - Array of 15+ visualization entries with metadata
- `domains{}` - 4 career domains with colors and descriptions
- `categories{}` - 4 visualization categories (timeline, technology, business, projects)
- `summary_stats` - Aggregate statistics for header display

**Adding New Visualizations:**
1. Generate matplotlib image (300 DPI PNG)
2. Copy to appropriate `visual/` directory
3. Update `career-highlights-config.json` with new entry
4. Copy image to web gallery `images/full/` directory

## Testing Approach

**Python Visualizations:**
- No formal test framework - manual validation of generated images
- Scripts include error handling for data processing
- Output validation through visual inspection

**Web Gallery:**
- Manual testing across browsers and devices
- Use browser dev tools for responsive design testing
- Test lightbox navigation and filtering functionality

## Performance Notes

**Python Generation:**
- 3-8 seconds per visualization
- <150MB memory usage per script
- Relative paths ensure portability

**Web Gallery:**
- Lighthouse score target: 90+
- Service worker provides offline support
- Lazy loading for images
- Mobile-optimized touch interactions

## Development Patterns

**Python Scripts:**
- Self-contained with embedded data or JSON file reading
- Consistent output to `../visual/` directories
- 300 DPI PNG output for publication quality
- Matplotlib styling with consistent color schemes

**Web Component:**
- Vanilla JavaScript ES6+ (no framework dependencies)
- Event-driven architecture with delegation
- CSS Grid and Flexbox for responsive layouts
- Progressive enhancement approach