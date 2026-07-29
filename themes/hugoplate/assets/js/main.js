// main script
(function () {
  "use strict";

  // Navigation dropdowns
  // ----------------------------------------
  const navbar = document.querySelector(".navbar");

  if (navbar) {
    const navToggle = navbar.querySelector("#nav-toggle");
    const dropdownToggles = Array.from(
      navbar.querySelectorAll(".nav-dropdown > input[type='checkbox']"),
    );

    const closeDropdowns = (except) => {
      dropdownToggles.forEach((toggle) => {
        if (toggle !== except) {
          toggle.checked = false;
        }
      });
    };

    dropdownToggles.forEach((toggle) => {
      toggle.addEventListener("change", () => {
        if (toggle.checked) {
          closeDropdowns(toggle);
        }
      });
    });

    navbar.querySelectorAll("#nav-menu a").forEach((link) => {
      link.addEventListener("click", () => {
        closeDropdowns();
        if (navToggle) {
          navToggle.checked = false;
        }
      });
    });

    document.addEventListener("click", (event) => {
      if (!navbar.contains(event.target)) {
        closeDropdowns();
      }
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        closeDropdowns();
        if (navToggle) {
          navToggle.checked = false;
        }
      }
    });
  }

  // Testimonial Slider
  // ----------------------------------------
  new Swiper(".testimonial-slider", {
    spaceBetween: 24,
    loop: true,
    pagination: {
      el: ".testimonial-slider-pagination",
      type: "bullets",
      clickable: true,
    },
    breakpoints: {
      768: {
        slidesPerView: 2,
      },
      992: {
        slidesPerView: 3,
      },
    },
  });
})();
