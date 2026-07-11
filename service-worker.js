const CACHE_NAME = "todo-list-cache-v2"; // bump this every time you deploy changes

const urlsToCache = [
  "/",
  "/static/todobg.jpeg",      // replace with your actual cat background image
  "/static/icon-192.png",
  "/static/icon-512.png"
];

// Install: cache static files
self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(urlsToCache))
  );
  self.skipWaiting();
});

// Activate: clean up old caches
self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) return caches.delete(key);
        })
      )
    )
  );
  self.clients.claim();
});

// Fetch: network-first for pages, cache-first for static assets
self.addEventListener("fetch", (event) => {
  const isHTML = event.request.mode === "navigate";

  if (isHTML) {
    // Try live version first (fresh tasks), fallback to cached page if offline
    event.respondWith(
      fetch(event.request)
        .then((response) => {
          const clone = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
          return response;
        })
        .catch(() => caches.match(event.request))
    );
  } else {
    // Static assets: serve from cache first, fallback to network
    event.respondWith(
      caches.match(event.request).then((cached) => cached || fetch(event.request))
    );
  }
});