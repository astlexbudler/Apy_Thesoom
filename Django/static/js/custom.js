search = () => {
    const searchInput = document.getElementById('searchInput');
    location.href = '/?search=' + searchInput.value;
}