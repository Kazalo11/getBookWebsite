document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('generateButton').addEventListener('click', generateStory);
  document.getElementById('downloadButton').addEventListener('click', downloadPDF);
});



function generateStory() {
  console.log("Obtaining the story")
  fetch('/generate-story')
    .then(response => response.text())
    .then(function(data){
     document.getElementById('story').innerText = data;;
    });
}

function downloadPDF() {
  window.open('../download-pdf');
}
