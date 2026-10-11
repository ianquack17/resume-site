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
