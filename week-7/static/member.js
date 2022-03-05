let query = document.getElementById('query');
let update = document.getElementById('update');

function queryMembers() {
  let username = document.getElementById('queryName').value;
  fetch(`http://127.0.0.1:3000/api/members?username=${username}`)
    .then(response => response.json())
    .then(result => {
      let data = result.data;
      if (data) {
        document.getElementById('showName').innerHTML = data.name + ' (' + username + ')';
        document.getElementById('queryName').value = '';
      } else {   // 若 response 為 data: null
        document.getElementById('showName').innerHTML = '查無此會員';
      }
      })
    .catch(err => console.log('Error: ' + err))
}

function updateName() {
  let updateName = document.getElementById('updateName').value;
  fetch('http://127.0.0.1:3000/api/member', {
    method:'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ name: updateName })   // JavaScript => JSON
  })
    .then(response => response.json())   // JSON => JavaScript
    .then(result => {
      if (result.ok == true) {
        document.getElementById('showNewName').innerHTML = '更新成功';
        document.getElementById('updateName').value = '';
      } else if(result.error == true) {
        document.getElementById('showNewName').innerHTML = '更新失敗';
      }
    })
    .catch(err => console.log('Error: '+ err))
}


query.addEventListener('click', queryMembers)
update.addEventListener('click', updateName)
