document.addEventListener('DOMContentLoaded', function() {
    var newsItems = document.querySelectorAll('.news-item');
    newsItems.forEach(function(item) {
        item.addEventListener('click', function() {
            var fullText = this.querySelector('.full-text');
            if (fullText.style.display === 'none') {
                fullText.style.display = 'block';
            } else {
                fullText.style.display = 'none';
            }
        });
    });
});