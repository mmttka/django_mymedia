const gridItems = document.querySelectorAll('.grid-item');
gridItems.forEach(item => {
    item.addEventListener('mouseover', () => {
        item.style.color = '#fff';
    });
    item.addEventListener('mouseout', () => {
        item.style.color = '#000';
    });
});
