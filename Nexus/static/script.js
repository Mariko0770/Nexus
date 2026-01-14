function submitForm(e,listId,url){
    e.preventDefault();
    const form=e.target;
    const data=new FormData(form);
    fetch(url,{method:"POST",body:data}).then(res=>res.json()).then(resp=>{
        if(resp.success) location.reload();
    });
}

function deleteItem(table,id){
    fetch(`/delete/${table}/${id}`).then(res=>res.json()).then(resp=>{
        if(resp.success) location.reload();
    })
}

function showSection(id){
    document.querySelectorAll('.card-section').forEach(s=>s.style.display='none');
    document.getElementById(id).style.display='block';
}

window.onload=function(){showSection('home');}
