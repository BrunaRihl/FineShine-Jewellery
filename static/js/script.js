/* 
   Handles the interactive star rating feature. 
   It listens for mouse events on star icons to highlight them 
   based on the user's interaction.
*/
document.addEventListener('DOMContentLoaded', () => {
    const stars = document.querySelectorAll('.rating .fa-star');
    const ratingInput = document.getElementById('rating');

    stars.forEach(star => {
      star.addEventListener('mouseover', (e) => {
        const value = e.target.dataset.value;
        highlightStars(value);
      });

      star.addEventListener('mouseout', () => {
        highlightStars(ratingInput.value || 0);
      });

      star.addEventListener('click', (e) => {
        const value = e.target.dataset.value;
        ratingInput.value = value;
        highlightStars(value);
      });
    });

    function highlightStars(value) {
      stars.forEach((star, index) => {
        if (index < value) {
          star.classList.add('selected');
          star.classList.remove('fa-regular');
          star.classList.add('fa-solid');
        } else {
          star.classList.remove('selected');
          star.classList.remove('fa-solid');
          star.classList.add('fa-regular');
        }
      });
    }
  });
  

/* 
   Creates a dynamic glitter effect 
   by adding sparkling particles to the div with the 
   "glitter-effect" class.
*/
document.addEventListener("DOMContentLoaded", function() {
  const glitterEffect = document.querySelector(".glitter-effect");

  function createGlitterParticle() {
    const particle = document.createElement("div");
    particle.classList.add("glitter-particle");
    particle.style.top = `${Math.random() * 100}%`;
    particle.style.left = `${Math.random() * 100}%`;
    particle.style.animationDelay = `${Math.random() * 2}s`;
    glitterEffect.appendChild(particle);
  }

  setInterval(createGlitterParticle, 200);
});

  