createMovieListener()

function createMovieListener(){
    const movie_list = document.querySelectorAll('.card-movie')
    movie_list.forEach(movie => {
        movie.addEventListener('click',()=>{
            window.location.href = `../${movie.id}`
        })
    
    });
}