document.addEventListener('DOMContentLoaded', function() {
    // Funzioni per la pagina di registrazione
    if (document.getElementById('registrationForm')) {
        // ... (il tuo codice esistente per la pagina di registrazione) ...
    }

    // Funzioni per la pagina home
    if (document.getElementById('lista-studenti')) {
        const listaStudentiElement = document.getElementById('lista-studenti');

        function rimuoviStudente(index) {
            let studenti = localStorage.getItem('studenti');
            if (studenti) {
                const studentiArray = JSON.parse(studenti);
                studentiArray.splice(index, 1);
                localStorage.setItem('studenti', JSON.stringify(studentiArray));
                caricaStudenti();
            }
        }

        function caricaStudenti() {
            listaStudentiElement.innerHTML = '';

            const studenti = localStorage.getItem('studenti');
            if (studenti) {
                const studentiArray = JSON.parse(studenti);
                if (studentiArray.length > 0) {
                    studentiArray.forEach((studente, index) => {
                        const listItem = document.createElement('li');
                        listItem.textContent = `${studente.nome} ${studente.cognome} (${studente.corso})`;

                        const rimuoviButton = document.createElement('button');
                        rimuoviButton.textContent = 'Rimuovi';
                        rimuoviButton.classList.add('rimuovi-button');
                        rimuoviButton.addEventListener('click', function() {
                            rimuoviStudente(index);
                        });

                        listItem.appendChild(rimuoviButton);
                        listaStudentiElement.appendChild(listItem);
                    });
                } else {
                    const listItem = document.createElement('li');
                    listItem.textContent = 'Nessuno studente registrato ancora.';
                    listaStudentiElement.appendChild(listItem);
                }
            } else {
                const listItem = document.createElement('li');
                listItem.textContent = 'Nessuno studente registrato ancora.';
                listaStudentiElement.appendChild(listItem);
            }
        }


        caricaStudenti();


    }
});