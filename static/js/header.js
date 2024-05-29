const pathname = window.location.pathname;

let currentPage

if (pathname === '/') {
    currentPage = 'Index'
} else {
    currentPage = pathname.charAt(1).toUpperCase() + pathname.slice(2).toLowerCase()
}

document.querySelector(`#${currentPage}Nav`).classList.add('active')
