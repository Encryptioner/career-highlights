// Service Worker for Career Highlights Gallery
// Provides offline functionality and image caching

const CACHE_NAME = 'career-highlights-v1';
const CACHE_URLS = [
  './',
  './index.html',
  './styles/highlights.css',
  './components/HighlightsGallery.js',
  './config/career-highlights-config.json'
];

// Install event - cache essential files
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Caching essential files');
        return cache.addAll(CACHE_URLS);
      })
      .then(() => self.skipWaiting())
  );
});

// Activate event - clean up old caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(cacheNames => {
        return Promise.all(
          cacheNames.map(cacheName => {
            if (cacheName !== CACHE_NAME) {
              console.log('Deleting old cache:', cacheName);
              return caches.delete(cacheName);
            }
          })
        );
      })
      .then(() => self.clients.claim())
  );
});

// Fetch event - serve from cache, fallback to network
self.addEventListener('fetch', event => {
  // Only handle GET requests
  if (event.request.method !== 'GET') return;

  // Skip non-HTTP(S) requests (chrome-extension, moz-extension, etc.)
  if (!event.request.url.startsWith('http://') && !event.request.url.startsWith('https://')) {
    return;
  }

  // Skip requests with query parameters that may contain dynamic content
  const url = new URL(event.request.url);
  if (url.search.includes('_t=') || url.search.includes('timestamp=')) {
    return;
  }

  // Handle image requests with cache-first strategy
  if (event.request.url.includes('/images/')) {
    event.respondWith(
      caches.match(event.request)
        .then(response => {
          if (response) {
            return response;
          }

          return fetch(event.request)
            .then(response => {
              // Cache successful image responses
              if (response.status === 200 && response.type === 'basic') {
                const responseClone = response.clone();
                caches.open(CACHE_NAME)
                  .then(cache => cache.put(event.request, responseClone))
                  .catch(error => {
                    console.log('Cache put failed:', error);
                  });
              }
              return response;
            })
            .catch(() => {
              // Return placeholder image if offline and not cached
              return new Response(`
                <svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
                  <rect width="400" height="300" fill="#f0f0f0"/>
                  <text x="200" y="150" text-anchor="middle" fill="#999" font-family="Arial">
                    Image not available offline
                  </text>
                </svg>
              `, {
                headers: { 'Content-Type': 'image/svg+xml' }
              });
            });
        })
    );
    return;
  }

  // Handle other requests with network-first strategy
  event.respondWith(
    fetch(event.request)
      .then(response => {
        // Cache successful responses
        if (response.status === 200 && response.type === 'basic') {
          const responseClone = response.clone();
          caches.open(CACHE_NAME)
            .then(cache => cache.put(event.request, responseClone))
            .catch(error => {
              console.log('Cache put failed:', error);
            });
        }
        return response;
      })
      .catch(() => {
        // Fallback to cache if network fails
        return caches.match(event.request)
          .then(response => {
            if (response) {
              return response;
            }

            // Return offline page for navigation requests
            if (event.request.mode === 'navigate') {
              return new Response(`
                <!DOCTYPE html>
                <html>
                <head>
                  <title>Offline - Career Highlights</title>
                  <style>
                    body {
                      font-family: Arial, sans-serif;
                      text-align: center;
                      padding: 2rem;
                      background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                      min-height: 100vh;
                      margin: 0;
                      display: flex;
                      align-items: center;
                      justify-content: center;
                      flex-direction: column;
                    }
                    .offline-content {
                      background: white;
                      padding: 2rem;
                      border-radius: 12px;
                      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                      max-width: 500px;
                    }
                    h1 { color: #2C3E50; }
                    p { color: #7F8C8D; line-height: 1.6; }
                    button {
                      background: #45B7D1;
                      color: white;
                      border: none;
                      padding: 1rem 2rem;
                      border-radius: 25px;
                      cursor: pointer;
                      font-weight: 600;
                      margin-top: 1rem;
                    }
                  </style>
                </head>
                <body>
                  <div class="offline-content">
                    <h1>📊 You're Offline</h1>
                    <p>The Career Highlights gallery requires an internet connection to load the visualizations.</p>
                    <p>Please check your connection and try again.</p>
                    <button onclick="location.reload()">Try Again</button>
                  </div>
                </body>
                </html>
              `, {
                headers: { 'Content-Type': 'text/html' }
              });
            }

            return new Response('Network error', {
              status: 408,
              headers: { 'Content-Type': 'text/plain' }
            });
          });
      })
  );
});

// Background sync for future enhancements
self.addEventListener('sync', event => {
  if (event.tag === 'background-sync') {
    console.log('Background sync triggered');
  }
});

// Push notifications for updates (future enhancement)
self.addEventListener('push', event => {
  if (event.data) {
    const data = event.data.json();
    const options = {
      body: data.body,
      icon: './images/favicon.png',
      badge: './images/badge.png',
      tag: 'career-highlights-update'
    };

    event.waitUntil(
      self.registration.showNotification(data.title, options)
    );
  }
});

// Notification click handling
self.addEventListener('notificationclick', event => {
  event.notification.close();

  event.waitUntil(
    clients.openWindow('./')
  );
});