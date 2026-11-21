document.addEventListener('DOMContentLoaded', function(){
  const loginToggle = document.getElementById('login-toggle');
  if(loginToggle){
    loginToggle.addEventListener('click', ()=> alert('Preview login not active. Use test@example.com in the real app'))
  }

  const uploadForm = document.getElementById('upload-form');
  if(uploadForm){
    uploadForm.addEventListener('submit', function(e){
      e.preventDefault();
      alert('This is a static preview. In the real app the file would upload and be queued for processing.')
    })
  }
})
