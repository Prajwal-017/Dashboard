document.addEventListener("DOMContentLoaded", () => {
  const shrink_btn = document.querySelector(".shrink-btn");
  const sidebar_links = document.querySelectorAll(".sidebar-links a");

  // Event listener for the shrink button
  shrink_btn.addEventListener("click", () => {
    document.body.classList.toggle("shrink");
  });

  // Event listener for sidebar links
  sidebar_links.forEach(link => {
    link.addEventListener("click", (event) => {
      // Prevent the sidebar from expanding when a link is clicked
      if (document.body.classList.contains("shrink")) {
        event.preventDefault(); // Prevent default behavior if needed
        // Optionally, handle navigation manually if using single-page applications
        window.location.href = link.getAttribute("href");
      }
    });
  });
});

  window.addEventListener('load', function() {
    var loaderWrapper = document.getElementById('loader-wrapper');
    loaderWrapper.style.display = 'none';
  });

