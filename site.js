const header = document.querySelector(".header");
const menuToggle = document.querySelector(".menu-toggle");
const nav = document.querySelector(".nav");

const closeMenu = () => {
    if (!header || !menuToggle) return;

    header.classList.remove("nav-open");
    menuToggle.setAttribute("aria-expanded", "false");
    menuToggle.setAttribute("aria-label", "Open navigation menu");
};

if (header && menuToggle && nav) {
    menuToggle.addEventListener("click", () => {
        const isOpen = header.classList.toggle("nav-open");
        menuToggle.setAttribute("aria-expanded", String(isOpen));
        menuToggle.setAttribute(
            "aria-label",
            isOpen ? "Close navigation menu" : "Open navigation menu"
        );
    });

    nav.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", closeMenu);
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") closeMenu();
    });

    window.addEventListener("resize", () => {
        if (window.innerWidth > 700) closeMenu();
    });
}

const carousel = document.querySelector(".panorama-carousel");
const prefersReducedMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
).matches;

if (carousel && !prefersReducedMotion) {
    window.setInterval(() => {
        const items = carousel.querySelectorAll(".panorama-item");

        if (items.length > 1) {
            carousel.appendChild(items[0]);
        }
    }, 3000);
}
