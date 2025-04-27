function filtrarEventos() {
    const culturaChecked = document.getElementById('culturaCheckbox').checked;
    const turismoChecked = document.getElementById('turismoCheckbox').checked;
  
    const cards = document.querySelectorAll('.card');
  
    cards.forEach(card => {
      const categoria = card.getAttribute('data-categoria');
  
      if (
        (categoria === 'Cultura' && culturaChecked) ||
        (categoria === 'Turismo' && turismoChecked) ||
        (!culturaChecked && !turismoChecked)
      ) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }
  