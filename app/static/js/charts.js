function makeChart(id, config) {
  const el = document.getElementById(id);
  if (!el) return;
  new Chart(el, config);
}

makeChart('salesChart', {
  type: 'bar',
  data: {
    labels: ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin'],
    datasets: [{
      label: 'Ventes (F)',
      data: [7000, 11000, 10500, 12500, 16000, 18000],
      backgroundColor: '#5cb7e6'
    }]
  }
});

makeChart('stockoutChart', {
  type: 'bar',
  data: {
    labels: ['Riz 50kg', 'Huile 1L', 'Sucre 1kg', 'Pâtes 500g', 'Lait 1L'],
    datasets: [{
      label: 'Rupture',
      data: [5, 4, 3, 2, 2],
      backgroundColor: ['#339fbd', '#ff8c3a', '#ffb13b', '#42a7ce', '#ef5548']
    }]
  }
});

makeChart('profitChart', {
  type: 'line',
  data: {
    labels: ['Sem 1', 'Sem 2', 'Sem 3', 'Sem 4', 'Sem 5'],
    datasets: [
      { label: 'Ventes', data: [2100, 3100, 3600, 2800, 4100], borderColor: '#51c7bb', fill: false },
      { label: 'Bénéfices', data: [1200, 1700, 2900, 2500, 3400], borderColor: '#ff8c3a', fill: false }
    ]
  }
});
