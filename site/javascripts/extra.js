// Externe Navigationseintraege (z. B. "legacy Doku") in einem neuen Tab oeffnen.
(function () {
  function externeLinksMarkieren() {
    document.querySelectorAll(".md-nav a[href]").forEach(function (link) {
      if (link.host && link.host !== location.host) {
        link.target = "_blank";
        link.rel = "noopener noreferrer";
      }
    });
  }

  // document$ feuert bei Instant Navigation nach jedem Seitenwechsel erneut
  if (typeof document$ !== "undefined") {
    document$.subscribe(externeLinksMarkieren);
  } else {
    document.addEventListener("DOMContentLoaded", externeLinksMarkieren);
  }
})();
