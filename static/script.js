function navigateTo(sectionId) {
    const carousel = document.getElementById('carousel');
    const section = document.getElementById(sectionId);

    if (!carousel || !section) return;

    const sectionRect = section.getBoundingClientRect();
    const carouselRect = carousel.getBoundingClientRect();

    const scrollAmount = sectionRect.left - carouselRect.left;
    carousel.style.transform = `translateX(-${scrollAmount}px)`;

    // Update active state in the navigation menu
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => link.classList.remove('active'));
    
    // Find the active link by matching onclick function content
    navLinks.forEach(link => {
        const onclickContent = link.getAttribute('onclick');
        if (onclickContent && onclickContent.includes(sectionId)) {
            link.classList.add('active');
        }
    });
}

// Grade color coding function
function applyGradeColoring() {
    const grades = document.querySelectorAll('.grade[data-note][data-max]');
    
    grades.forEach(grade => {
        const note = parseFloat(grade.getAttribute('data-note'));
        const max = parseFloat(grade.getAttribute('data-max'));
        
        if (max > 0) {
            const percentage = (note / max) * 100;
            
            // Remove existing grade classes
            grade.classList.remove('excellent', 'good', 'average', 'below-average', 'poor');
            
            // Apply color coding based on percentage
            if (percentage >= 85) {
                grade.classList.add('excellent');
            } else if (percentage >= 70) {
                grade.classList.add('good');
            } else if (percentage >= 50) {
                grade.classList.add('average');
            } else if (percentage >= 30) {
                grade.classList.add('below-average');
            } else {
                grade.classList.add('poor');
            }
            
            // Add percentage display
            const percentageText = ` (${percentage.toFixed(1)}%)`;
            if (!grade.textContent.includes('%')) {
                grade.textContent += percentageText;
            }
        }
    });
}

// Calculate subject statistics
function calculateSubjectStats() {
    const subjects = document.querySelectorAll('.subject-container');
    
    subjects.forEach(subject => {
        const grades = subject.querySelectorAll('.grade[data-note][data-max][data-coef]');
        let totalPoints = 0;
        let totalMaxPoints = 0;
        let totalCoeff = 0;
        let percentages = [];
        
        grades.forEach(grade => {
            const note = parseFloat(grade.getAttribute('data-note'));
            const max = parseFloat(grade.getAttribute('data-max'));
            const coef = parseFloat(grade.getAttribute('data-coef'));
            
            if (max > 0 && coef > 0) {
                const percentage = (note / max) * 100;
                totalPoints += note * coef;
                totalMaxPoints += max * coef;
                totalCoeff += coef;
                percentages.push(percentage);
            }
        });
        
        // Calculate weighted average
        const weightedAverage = totalMaxPoints > 0 ? (totalPoints / totalMaxPoints) * 20 : 0;
        
        // Find min and max percentages
        const minPercentage = percentages.length > 0 ? Math.min(...percentages) : 0;
        const maxPercentage = percentages.length > 0 ? Math.max(...percentages) : 0;
        
        // Update display
        const countElement = subject.querySelector('.subject-count');
        const avgElement = subject.querySelector('.subject-avg');
        const maxElement = subject.querySelector('.subject-max');
        const minElement = subject.querySelector('.subject-min');
        
        if (countElement) countElement.textContent = grades.length;
        if (avgElement) avgElement.textContent = weightedAverage.toFixed(1) + '/20';
        if (maxElement) maxElement.textContent = maxPercentage.toFixed(1) + '%';
        if (minElement) minElement.textContent = minPercentage.toFixed(1) + '%';
        
        // Color code the subject average
        const avgDisplay = subject.querySelector('.subject-average');
        if (avgDisplay && weightedAverage > 0) {
            const avgPercentage = (weightedAverage / 20) * 100;
            let colorClass = '';
            if (avgPercentage >= 85) colorClass = 'excellent';
            else if (avgPercentage >= 70) colorClass = 'good';
            else if (avgPercentage >= 50) colorClass = 'average';
            else if (avgPercentage >= 30) colorClass = 'below-average';
            else colorClass = 'poor';
            
            avgDisplay.textContent = `(Moy: ${weightedAverage.toFixed(1)}/20)`;
            avgDisplay.className = `subject-average grade ${colorClass}`;
        }
    });
}

// Apply grade coloring when page loads
document.addEventListener('DOMContentLoaded', function() {
    applyGradeColoring();
    calculateSubjectStats();
});

