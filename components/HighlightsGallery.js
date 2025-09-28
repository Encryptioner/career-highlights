/**
 * Career Highlights Gallery Component
 * Displays visualization gallery with filtering, lightbox, and responsive design
 */
class HighlightsGallery {
  constructor(containerId, configPath = './config/career-highlights-config.json') {
    this.container = document.getElementById(containerId);
    this.configPath = configPath;
    this.config = null;
    this.currentFilter = 'all';
    this.currentDomain = 'all';
    this.currentLightboxIndex = 0;
    this.filteredVisualizations = [];

    // Zoom state management
    this.zoomLevel = 1;
    this.maxZoom = 4;
    this.minZoom = 0.5;
    this.zoomStep = 0.25;
    this.panX = 0;
    this.panY = 0;
    this.isPanning = false;
    this.lastPanX = 0;
    this.lastPanY = 0;

    // Create a promise that resolves when initialization is complete
    this.ready = this.init();
  }

  async init() {
    try {
      await this.loadConfig();
      this.render();
      this.bindEvents();

      // Add a small delay to ensure DOM is fully rendered
      await new Promise(resolve => requestAnimationFrame(resolve));

      return this; // Return this for chaining
    } catch (error) {
      console.error('Failed to initialize HighlightsGallery:', error);
      this.renderError();
      throw error; // Re-throw to handle in loading logic
    }
  }

  /**
   * Get the correct image path based on domain
   */
  getImagePath(visualization) {
    const org = this.config.file_organization;
    switch (visualization.domain) {
      case 'personal':
        return `${org.personal_career}${visualization.file}`;
      case 'professional':
        return `${org.professional_career}${visualization.file}`;
      case 'personal-projects':
        return `${org.personal_projects}${visualization.file}`;
      case 'professional-projects':
        return `${org.professional_projects}${visualization.file}`;
      default:
        return `${org.base_path}${visualization.file}`;
    }
  }

  async loadConfig() {
    // Start config fetch immediately
    const configPromise = fetch(this.configPath);

    const response = await configPromise;
    if (!response.ok) {
      throw new Error(`Failed to load config: ${response.statusText}`);
    }
    this.config = await response.json();
    this.filteredVisualizations = [...this.config.visualizations];
  }

  render() {
    if (!this.config) return;

    this.container.innerHTML = `
      <div class="highlights-container" style="opacity: 0; transition: opacity 0.3s ease-in;">
        ${this.renderHeader()}
        ${this.renderDomainTabs()}
        ${this.renderFilters()}
        ${this.renderGallery()}
        ${this.renderLightbox()}
      </div>
    `;

    // Trigger fade-in after content is inserted
    requestAnimationFrame(() => {
      const container = this.container.querySelector('.highlights-container');
      if (container) {
        container.style.opacity = '1';
      }
    });
  }

  renderHeader() {
    const stats = this.config.summary_stats;
    return `
      <div class="highlights-header">
        <h1 class="highlights-title">${this.config.metadata.title}</h1>
        <p class="highlights-subtitle">${this.config.metadata.description}</p>

        <div class="highlights-stats">
          <div class="stat-item">
            <span class="stat-number">${stats.total_years_tracked}</span>
            <span class="stat-label">Years Tracked</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">${stats.personal_projects + stats.professional_projects}</span>
            <span class="stat-label">Total Projects</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">${stats.total_users_impacted}</span>
            <span class="stat-label">Users Impacted</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">${stats.visualizations_generated}</span>
            <span class="stat-label">Visualizations</span>
          </div>
        </div>
      </div>
    `;
  }

  renderDomainTabs() {
    const domains = Object.entries(this.config.domains);

    return `
      <div class="domain-tabs">
        <button class="domain-tab ${this.currentDomain === 'all' ? 'active' : ''}"
                data-domain="all">
          🌟 All Domains
        </button>
        ${domains.map(([key, domain]) => `
          <button class="domain-tab ${this.currentDomain === key ? 'active' : ''}"
                  data-domain="${key}"
                  style="border-top-color: ${domain.color};">
            ${domain.name}
          </button>
        `).join('')}
      </div>
    `;
  }

  renderFilters() {
    const categories = Object.entries(this.config.categories);

    return `
      <div class="highlights-filters">
        <button class="filter-btn ${this.currentFilter === 'all' ? 'active' : ''}"
                data-filter="all">
          <span class="icon">🔍</span> All Categories
        </button>
        <button class="filter-btn ${this.currentFilter === 'featured' ? 'active' : ''}"
                data-filter="featured">
          <span class="icon">⭐</span> Featured
        </button>
        ${categories.map(([key, category]) => `
          <button class="filter-btn ${this.currentFilter === key ? 'active' : ''}"
                  data-filter="${key}">
            <span class="icon">${category.icon}</span> ${category.name}
          </button>
        `).join('')}
      </div>
    `;
  }

  renderGallery() {
    if (this.filteredVisualizations.length === 0) {
      return `
        <div class="no-results">
          <h3>No visualizations found</h3>
          <p>Try adjusting your filters to see more results.</p>
        </div>
      `;
    }

    return `
      <div class="highlights-gallery">
        ${this.filteredVisualizations.map((viz, index) => this.renderVisualizationCard(viz, index)).join('')}
      </div>
    `;
  }

  renderVisualizationCard(viz, index) {
    const domain = this.config.domains[viz.domain];
    const category = this.config.categories[viz.category];

    return `
      <div class="visualization-card ${viz.featured ? 'featured' : ''}"
           data-index="${index}"
           data-viz-id="${viz.id}"
           data-category="${viz.category}"
           data-domain="${viz.domain}">

        <img src="${this.getImagePath(viz)}"
             alt="${viz.title}"
             class="card-image"
             loading="lazy"
             onerror="this.src='./images/placeholder.png'">

        <div class="card-content">
          <h3 class="card-title">${viz.title}</h3>
          <p class="card-description">${viz.description}</p>

          <div class="card-metrics">
            ${viz.metrics.map(metric => `
              <span class="metric-tag">${metric}</span>
            `).join('')}
          </div>

          <div class="card-footer">
            <span class="card-category" style="background: ${category.color};">
              ${category.icon} ${category.name}
            </span>
            <span class="card-domain" style="color: ${domain.color};">
              ${domain.name}
            </span>
          </div>
        </div>
      </div>
    `;
  }

  renderLightbox() {
    return `
      <div class="lightbox" id="lightbox">
        <div class="lightbox-content">
          <button class="lightbox-close" id="lightbox-close" title="Close">&times;</button>
          <button class="lightbox-nav lightbox-prev" id="lightbox-prev" title="Previous">&#8249;</button>
          <button class="lightbox-nav lightbox-next" id="lightbox-next" title="Next">&#8250;</button>
          <button class="lightbox-download" id="lightbox-download" title="Download Image">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 16l-4-4h3V4h2v8h3l-4 4zm-7 4h14v2H5v-2z"/>
            </svg>
          </button>

          <!-- Zoom Controls -->
          <div class="lightbox-zoom-controls">
            <button class="zoom-btn" id="zoom-out" title="Zoom Out">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M15.5 14h-.79l-.28-.27c1.2-1.4 1.82-3.31 1.48-5.34-0.47-2.78-2.79-5-5.59-5.34-4.23-0.52-7.79 3.04-7.27 7.27 0.34 2.8 2.56 5.12 5.34 5.59 2.03 0.34 3.94-0.28 5.34-1.48l0.27 0.28v0.79l4.25 4.25c0.41 0.41 1.08 0.41 1.49 0 0.41-0.41 0.41-1.08 0-1.49L15.5 14zM9.5 14C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
                <path d="M7 9h5v1H7z"/>
              </svg>
            </button>
            <span class="zoom-level" id="zoom-level">100%</span>
            <button class="zoom-btn" id="zoom-in" title="Zoom In">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M15.5 14h-.79l-.28-.27c1.2-1.4 1.82-3.31 1.48-5.34-0.47-2.78-2.79-5-5.59-5.34-4.23-0.52-7.79 3.04-7.27 7.27 0.34 2.8 2.56 5.12 5.34 5.59 2.03 0.34 3.94-0.28 5.34-1.48l0.27 0.28v0.79l4.25 4.25c0.41 0.41 1.08 0.41 1.49 0 0.41-0.41 0.41-1.08 0-1.49L15.5 14zM9.5 14C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
                <path d="M12 10h-2v2H9v-2H7V9h2V7h1v2h2v1z"/>
              </svg>
            </button>
            <button class="zoom-btn" id="zoom-reset" title="Reset Zoom">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
              </svg>
            </button>
          </div>

          <div class="lightbox-image-container" id="lightbox-image-container">
            <img src="" alt="" class="lightbox-image" id="lightbox-image">
          </div>
        </div>
      </div>
    `;
  }

  bindEvents() {
    // Filter buttons
    this.container.addEventListener('click', (e) => {
      if (e.target.matches('.filter-btn') || e.target.closest('.filter-btn')) {
        const btn = e.target.closest('.filter-btn');
        const filter = btn.dataset.filter;
        this.setFilter(filter);
      }
    });

    // Domain tabs
    this.container.addEventListener('click', (e) => {
      if (e.target.matches('.domain-tab') || e.target.closest('.domain-tab')) {
        const btn = e.target.closest('.domain-tab');
        const domain = btn.dataset.domain;
        this.setDomain(domain);
      }
    });

    // Visualization cards
    this.container.addEventListener('click', (e) => {
      if (e.target.matches('.visualization-card') || e.target.closest('.visualization-card')) {
        const card = e.target.closest('.visualization-card');
        const index = parseInt(card.dataset.index);
        this.openLightbox(index);
      }
    });

    // Lightbox controls
    this.bindLightboxEvents();

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      const lightbox = document.getElementById('lightbox');
      if (lightbox.classList.contains('active')) {
        switch(e.key) {
          case 'Escape':
            this.closeLightbox();
            break;
          case 'ArrowLeft':
            this.previousImage();
            break;
          case 'ArrowRight':
            this.nextImage();
            break;
          case '+':
          case '=':
            e.preventDefault();
            this.zoomIn();
            break;
          case '-':
            e.preventDefault();
            this.zoomOut();
            break;
          case '0':
            e.preventDefault();
            this.resetZoom();
            break;
        }
      }
    });
  }

  bindLightboxEvents() {
    const lightbox = document.getElementById('lightbox');
    const closeBtn = document.getElementById('lightbox-close');
    const prevBtn = document.getElementById('lightbox-prev');
    const nextBtn = document.getElementById('lightbox-next');
    const downloadBtn = document.getElementById('lightbox-download');
    const zoomInBtn = document.getElementById('zoom-in');
    const zoomOutBtn = document.getElementById('zoom-out');
    const zoomResetBtn = document.getElementById('zoom-reset');
    const imageContainer = document.getElementById('lightbox-image-container');
    const image = document.getElementById('lightbox-image');

    // Close lightbox
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) {
        this.closeLightbox();
      }
    });

    closeBtn.addEventListener('click', () => this.closeLightbox());
    prevBtn.addEventListener('click', () => this.previousImage());
    nextBtn.addEventListener('click', () => this.nextImage());
    downloadBtn.addEventListener('click', () => this.downloadImage());

    // Zoom controls
    zoomInBtn.addEventListener('click', () => this.zoomIn());
    zoomOutBtn.addEventListener('click', () => this.zoomOut());
    zoomResetBtn.addEventListener('click', () => this.resetZoom());

    // Mouse wheel zoom
    imageContainer.addEventListener('wheel', (e) => {
      e.preventDefault();
      const rect = imageContainer.getBoundingClientRect();
      const centerX = (e.clientX - rect.left) / rect.width;
      const centerY = (e.clientY - rect.top) / rect.height;

      if (e.deltaY < 0) {
        this.zoomAt(centerX, centerY, this.zoomStep);
      } else {
        this.zoomAt(centerX, centerY, -this.zoomStep);
      }
    });

    // Pan functionality
    let isDragging = false;
    let startX = 0;
    let startY = 0;
    let startPanX = 0;
    let startPanY = 0;

    image.addEventListener('mousedown', (e) => {
      if (this.zoomLevel > 1) {
        isDragging = true;
        startX = e.clientX;
        startY = e.clientY;
        startPanX = this.panX;
        startPanY = this.panY;
        image.style.cursor = 'grabbing';
        e.preventDefault();
      }
    });

    document.addEventListener('mousemove', (e) => {
      if (isDragging && this.zoomLevel > 1) {
        const deltaX = e.clientX - startX;
        const deltaY = e.clientY - startY;
        this.panX = startPanX + deltaX;
        this.panY = startPanY + deltaY;
        this.updateImageTransform();
      }
    });

    document.addEventListener('mouseup', () => {
      if (isDragging) {
        isDragging = false;
        image.style.cursor = this.zoomLevel > 1 ? 'grab' : 'default';
      }
    });

    // Touch gestures for mobile
    let touchStartX = 0;
    let touchStartY = 0;
    let touchStartPanX = 0;
    let touchStartPanY = 0;
    let isTouchPanning = false;
    let initialTouchDistance = 0;
    let initialZoom = 1;

    imageContainer.addEventListener('touchstart', (e) => {
      e.preventDefault();

      if (e.touches.length === 1) {
        // Single touch - start panning
        if (this.zoomLevel > 1) {
          isTouchPanning = true;
          touchStartX = e.touches[0].clientX;
          touchStartY = e.touches[0].clientY;
          touchStartPanX = this.panX;
          touchStartPanY = this.panY;
        } else {
          // Store for swipe detection
          touchStartX = e.touches[0].clientX;
        }
      } else if (e.touches.length === 2) {
        // Two touches - start pinch zoom
        isTouchPanning = false;
        const touch1 = e.touches[0];
        const touch2 = e.touches[1];
        initialTouchDistance = Math.sqrt(
          Math.pow(touch2.clientX - touch1.clientX, 2) +
          Math.pow(touch2.clientY - touch1.clientY, 2)
        );
        initialZoom = this.zoomLevel;
      }
    });

    imageContainer.addEventListener('touchmove', (e) => {
      e.preventDefault();

      if (e.touches.length === 1 && isTouchPanning) {
        // Single touch panning
        const deltaX = e.touches[0].clientX - touchStartX;
        const deltaY = e.touches[0].clientY - touchStartY;
        this.panX = touchStartPanX + deltaX;
        this.panY = touchStartPanY + deltaY;
        this.updateImageTransform();
      } else if (e.touches.length === 2) {
        // Two touch pinch zoom
        const touch1 = e.touches[0];
        const touch2 = e.touches[1];
        const currentDistance = Math.sqrt(
          Math.pow(touch2.clientX - touch1.clientX, 2) +
          Math.pow(touch2.clientY - touch1.clientY, 2)
        );

        const scale = currentDistance / initialTouchDistance;
        const newZoom = Math.min(this.maxZoom, Math.max(this.minZoom, initialZoom * scale));
        this.setZoom(newZoom);
      }
    });

    imageContainer.addEventListener('touchend', (e) => {
      if (e.touches.length === 0) {
        if (!isTouchPanning && e.changedTouches.length === 1) {
          // Check for swipe gesture
          const endX = e.changedTouches[0].clientX;
          const diff = touchStartX - endX;

          if (Math.abs(diff) > 50) { // Minimum swipe distance
            if (diff > 0) {
              this.nextImage();
            } else {
              this.previousImage();
            }
          }
        }
        isTouchPanning = false;
      }
    });

    // Double-tap to zoom
    let lastTap = 0;
    imageContainer.addEventListener('touchend', (e) => {
      const currentTime = new Date().getTime();
      const tapLength = currentTime - lastTap;
      if (tapLength < 500 && tapLength > 0 && e.touches.length === 0) {
        e.preventDefault();
        if (this.zoomLevel === 1) {
          this.setZoom(2);
        } else {
          this.resetZoom();
        }
      }
      lastTap = currentTime;
    });
  }

  setFilter(filter) {
    this.currentFilter = filter;
    this.updateFilteredVisualizations();
    this.updateUI();

    // Debug info
    console.log(`Filter changed to: ${filter}, showing ${this.filteredVisualizations.length} results`);
  }

  setDomain(domain) {
    this.currentDomain = domain;
    this.updateFilteredVisualizations();
    this.updateUI();

    // Debug info
    console.log(`Domain changed to: ${domain}, showing ${this.filteredVisualizations.length} results`);
  }

  updateFilteredVisualizations() {
    // Ensure we always start with the full dataset
    if (!this.config || !this.config.visualizations) {
      console.error('Config or visualizations not available');
      this.filteredVisualizations = [];
      return;
    }

    this.filteredVisualizations = this.config.visualizations.filter(viz => {
      let matchesFilter = true;
      let matchesDomain = true;

      // Apply category filter
      if (this.currentFilter !== 'all') {
        if (this.currentFilter === 'featured') {
          matchesFilter = viz.featured === true;
        } else {
          matchesFilter = viz.category === this.currentFilter;
        }
      }

      // Apply domain filter
      if (this.currentDomain !== 'all') {
        matchesDomain = viz.domain === this.currentDomain;
      }

      return matchesFilter && matchesDomain;
    });

    // Debug output
    console.log(`Filtered ${this.config.visualizations.length} visualizations to ${this.filteredVisualizations.length} results`);
    console.log(`Current filters - Filter: ${this.currentFilter}, Domain: ${this.currentDomain}`);
  }

  updateUI() {
    // Update filter buttons
    this.container.querySelectorAll('.filter-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.filter === this.currentFilter);
    });

    // Update domain tabs
    this.container.querySelectorAll('.domain-tab').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.domain === this.currentDomain);
    });

    // Re-render gallery - use innerHTML to preserve container and event bindings
    const galleryContainer = this.container.querySelector('.highlights-gallery, .no-results');
    if (galleryContainer) {
      // Create a temporary container to get the new content
      const tempDiv = document.createElement('div');
      tempDiv.innerHTML = this.renderGallery();

      // Replace the existing gallery content with new content
      galleryContainer.parentNode.replaceChild(tempDiv.firstElementChild, galleryContainer);
    } else {
      // If no gallery container exists, find where to insert it
      const filterContainer = this.container.querySelector('.highlights-filters');
      if (filterContainer) {
        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = this.renderGallery();
        filterContainer.insertAdjacentElement('afterend', tempDiv.firstElementChild);
      }
    }

    // Add fade-in animation
    const cards = this.container.querySelectorAll('.visualization-card');
    cards.forEach((card, index) => {
      card.style.animationDelay = `${index * 0.1}s`;
      card.classList.add('fade-in-up');
    });
  }

  openLightbox(index) {
    this.currentLightboxIndex = index;
    const viz = this.filteredVisualizations[index];
    const lightbox = document.getElementById('lightbox');

    // Reset zoom state
    this.resetZoom();

    // Update lightbox content - only image
    document.getElementById('lightbox-image').src = this.getImagePath(viz);
    document.getElementById('lightbox-image').alt = viz.title;

    // Show lightbox
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden'; // Prevent body scroll
  }

  closeLightbox() {
    const lightbox = document.getElementById('lightbox');
    lightbox.classList.remove('active');
    document.body.style.overflow = ''; // Restore body scroll
  }

  previousImage() {
    if (this.currentLightboxIndex > 0) {
      this.currentLightboxIndex--;
    } else {
      // Wrap to last image
      this.currentLightboxIndex = this.filteredVisualizations.length - 1;
    }
    this.updateLightboxImage();
  }

  nextImage() {
    if (this.currentLightboxIndex < this.filteredVisualizations.length - 1) {
      this.currentLightboxIndex++;
    } else {
      // Wrap to first image
      this.currentLightboxIndex = 0;
    }
    this.updateLightboxImage();
  }

  updateLightboxImage() {
    const viz = this.filteredVisualizations[this.currentLightboxIndex];
    const img = document.getElementById('lightbox-image');

    // Reset zoom state when changing images
    this.resetZoom();

    // Fade out
    img.style.opacity = '0';

    setTimeout(() => {
      img.src = this.getImagePath(viz);
      img.alt = viz.title;

      // Fade in
      img.style.opacity = '1';
    }, 150);
  }

  downloadImage() {
    const viz = this.filteredVisualizations[this.currentLightboxIndex];
    const imageSrc = this.getImagePath(viz);

    // Create a temporary anchor element to trigger download
    const link = document.createElement('a');
    link.href = imageSrc;
    link.download = `${viz.title.replace(/[^a-zA-Z0-9]/g, '_')}_highlight.png`;

    // Append to body, click, and remove
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }

  renderError() {
    this.container.innerHTML = `
      <div class="error-container">
        <h2>Error Loading Gallery</h2>
        <p>Sorry, we couldn't load the career highlights gallery. Please try refreshing the page.</p>
      </div>
    `;
  }

  // Zoom control methods
  zoomIn() {
    const newZoom = Math.min(this.maxZoom, this.zoomLevel + this.zoomStep);
    this.setZoom(newZoom);
  }

  zoomOut() {
    const newZoom = Math.max(this.minZoom, this.zoomLevel - this.zoomStep);
    this.setZoom(newZoom);
  }

  resetZoom() {
    this.zoomLevel = 1;
    this.panX = 0;
    this.panY = 0;
    this.updateImageTransform();
    this.updateZoomLevel();

    const image = document.getElementById('lightbox-image');
    if (image) {
      image.style.cursor = 'default';
    }
  }

  setZoom(newZoom) {
    this.zoomLevel = Math.min(this.maxZoom, Math.max(this.minZoom, newZoom));
    this.updateImageTransform();
    this.updateZoomLevel();

    const image = document.getElementById('lightbox-image');
    if (image) {
      image.style.cursor = this.zoomLevel > 1 ? 'grab' : 'default';
    }
  }

  zoomAt(centerX, centerY, zoomDelta) {
    const oldZoom = this.zoomLevel;
    const newZoom = Math.min(this.maxZoom, Math.max(this.minZoom, oldZoom + zoomDelta));

    if (newZoom !== oldZoom) {
      const zoomFactor = newZoom / oldZoom;

      // Adjust pan to zoom towards the cursor position
      const imageContainer = document.getElementById('lightbox-image-container');
      if (imageContainer) {
        const rect = imageContainer.getBoundingClientRect();
        const offsetX = (centerX * rect.width - rect.width / 2);
        const offsetY = (centerY * rect.height - rect.height / 2);

        this.panX = this.panX * zoomFactor - offsetX * (zoomFactor - 1);
        this.panY = this.panY * zoomFactor - offsetY * (zoomFactor - 1);
      }

      this.zoomLevel = newZoom;
      this.updateImageTransform();
      this.updateZoomLevel();

      const image = document.getElementById('lightbox-image');
      if (image) {
        image.style.cursor = this.zoomLevel > 1 ? 'grab' : 'default';
      }
    }
  }

  updateImageTransform() {
    const image = document.getElementById('lightbox-image');
    if (image) {
      image.style.transform = `scale(${this.zoomLevel}) translate(${this.panX / this.zoomLevel}px, ${this.panY / this.zoomLevel}px)`;
      image.style.transformOrigin = 'center center';
    }
  }

  updateZoomLevel() {
    const zoomLevelElement = document.getElementById('zoom-level');
    if (zoomLevelElement) {
      zoomLevelElement.textContent = `${Math.round(this.zoomLevel * 100)}%`;
    }
  }
}

// Export for use
if (typeof module !== 'undefined' && module.exports) {
  module.exports = HighlightsGallery;
}