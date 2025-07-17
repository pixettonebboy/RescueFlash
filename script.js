// Inizializza Ruffle
window.RufflePlayer = window.RufflePlayer || {};

let player; // Variabile globale

window.addEventListener("load", () => {
  const ruffle = window.RufflePlayer.newest();
  const container = document.getElementById("flash-container");

  // Crea il player e carica il file SWF
  player = ruffle.createPlayer();
  container.innerHTML = "";
  container.appendChild(player);
  player.load("secure_TheChampions3.swf");

  // Bottone fullscreen
  const fullscreenBtn = document.getElementById("fullscreen-button");
  fullscreenBtn.addEventListener("click", () => {
    if (player.requestFullscreen) {
      player.requestFullscreen();
    } else if (player.webkitRequestFullscreen) {
      player.webkitRequestFullscreen();
    } else if (player.msRequestFullscreen) {
      player.msRequestFullscreen();
    } else {
      alert("Fullscreen non supportato nel tuo browser.");
    }
  });
});
