(function() {
    "use strict";
    const message = document.querySelector('#message');
    const result = document.querySelector('#result');
    const schema = document.querySelector('aside');
    const query = document.querySelector('#query');
    const form = document.querySelector('#sql');

    schema.querySelector('.widget').addEventListener('click', function() {
        const icon = this.querySelector('.widget-icon');
        if(schema.classList.contains('hidden')) {
            schema.classList.remove('hidden');
            icon.textContent = 'v';
        } else {
            schema.classList.add('hidden');
            icon.textContent = '^';
        }
    });

    form.addEventListener('submit', e => e.preventDefault());

    query.addEventListener('click', async () => {
        const res = await fetch(`/api/solve${window.location.search}`, {
            'method': 'POST',
            'credentials': 'include',
            'body': new FormData(form)
        });
        const json = await res.json();

        if(json.message) {
            message.classList.remove('hidden');
            message.textContent = json.message;
        }

        result.innerHTML = '';
        json.data.map(row => {
            const tr = document.createElement('tr');
            row.map(value => {
                const td = document.createElement('td');
                td.innerText = value;
                return td;
            }).forEach(td => tr.appendChild(td));
            return tr;
        }).forEach(tr => result.appendChild(tr));
    });
})();
