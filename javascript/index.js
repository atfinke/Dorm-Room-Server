
let effects = [
  "Color Burst",
  "Flames",
  "Forest",
  "Inner Peace",
  "Nemo",
  "Northern Lights",
  "Snowfall"
]

function loadEffects() {
  bodyHTML = "";
  for (let i = 0; i < effects.length; i++) {
    bodyHTML += '<tr onclick="updateEffect(this)"><td class="effects-data">' + effects[i] + '</td></tr>';
  }
  document.getElementById("effects-body").innerHTML = bodyHTML;
}

function updateEffect(x) {
  effect = effects[x.rowIndex];
  console.log(effect);

  alert("Lights will be set to " + effect + " within 30 seconds.")
}
