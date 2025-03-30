document.addEventListener("DOMContentLoaded", function () {
    const sections = document.querySelectorAll("section");

    function revealSections() {
        sections.forEach(section => {
            const sectionTop = section.getBoundingClientRect().top;
            if (sectionTop < window.innerHeight - 100) {
                section.style.opacity = "1";
                section.style.transform = "translateY(0)";
            }
        });
    }

    revealSections();
    window.addEventListener("scroll", revealSections);
});
