function submitForm(e, listId, url){
    e.preventDefault();
    const form = e.target;
    const data = new FormData(form);
    fetch(url,{method:"POST",body:data})
        .then(res=>res.json())
        .then(resp=>{
            if(resp.success) location.reload();
        });
}

function deleteItem(table,id){
    fetch(`/delete/${table}/${id}`)
        .then(res=>res.json())
        .then(resp=>{
            if(resp.success) location.reload();
        });
}

function showSection(id){
    document.querySelectorAll('.card-section').forEach(s=>s.style.display='none');
    document.getElementById(id).style.display='block';
}

window.onload=function(){showSection('home');}

function formatDateInput(input){
    input.addEventListener('input', e=>{
        let v = input.value.replace(/\D/g,'');
        if(v.length > 2) v = v.slice(0,2)+'/'+v.slice(2);
        if(v.length > 5) v = v.slice(0,5)+'/'+v.slice(5,9);
        input.value = v.slice(0,10);
    });
}

document.querySelectorAll('input[name="date"],input[name="birth_date"],input[name="start"],input[name="target"],input[name="due_date"],input[name="project_date"],input[name="event_date"]').forEach(formatDateInput);

function searchItems(e){
    if(e.key !== "Enter") return;
    e.preventDefault();

    let q = document.getElementById('searchInput').value.toLowerCase().trim();
    if(q === "") return;

    document.querySelectorAll('.card-section').forEach(section=>{
        let ul = section.querySelector('ul');
        let hasMatch = false;

        if(ul){
            let items = ul.querySelectorAll('li');
            items.forEach(li=>{
                if(li.textContent.toLowerCase().includes(q)){
                    li.style.display = 'flex';
                    hasMatch = true;
                } else {
                    li.style.display = 'none';
                }
            });
        }

        section.style.display = hasMatch ? 'block' : 'none';
    });
}
