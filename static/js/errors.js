window.addEventListener('load', () => {
    const message = document.getElementById('message');
    if (message) {
        setTimeout(() => {
            message.classList.add('show');
            setTimeout(() => {
                message.classList.add('hidden');
            }, 2000);
        });
    }
});
