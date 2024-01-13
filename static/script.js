function navigateTo(sectionId) {
    const carousel = document.getElementById('carousel');
    const section = document.getElementById(sectionId);

    const sectionRect = section.getBoundingClientRect();
    const carouselRect = carousel.getBoundingClientRect();

    const scrollAmount = sectionRect.left - carouselRect.left;
    carousel.style.transform = `translateX(-${scrollAmount}px)`;

    // Update active state in the navigation menu
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => link.classList.remove('active'));
    const activeLink = document.querySelector(`nav a[href="#${sectionId}"]`);
    activeLink.classList.add('active');
}

