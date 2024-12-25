function remove_year() {
    if (localStorage.getItem('selectedYear') !== null) {
        console.log('Removed year from localStorage:', localStorage.getItem('selectedYear'));
        localStorage.removeItem('selectedYear');
        config()
    }else{
        console.log('No year to remove from localStorage');
    }
}