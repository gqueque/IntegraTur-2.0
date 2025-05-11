// static/eventos/js/calendario.js

// Importa o core e o plugin DayGrid (se estiver usando ES modules/bundler)
import { Calendar } from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid';

// Quando o DOM estiver pronto, inicializa o calendário
document.addEventListener('DOMContentLoaded', function() {
  const calendarEl = document.getElementById('calendar');
  if (!calendarEl) return;

  const calendar = new Calendar(calendarEl, {
    plugins: [ dayGridPlugin ],
    initialView: 'dayGridMonth',
    headerToolbar: {
      left: 'prev,next today',
      center: 'title',
      right: ''
    },
    events: {
      url: '/eventos/api/events/',    // ou use {% url 'events_json' %} no template
      extraParams: () => ({
        category: document.getElementById('category-filter').value,
        location: document.getElementById('location-filter').value,
        type: document.getElementById('type-filter').value
      })
    }
  });

  calendar.render();

  // Refaz consulta quando algum filtro mudar
  ['category-filter','location-filter','type-filter'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.addEventListener('change', () => calendar.refetchEvents());
  });
});
