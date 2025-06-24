function saveData() {
  const inputValue = documents.getElementById("userInput").value;

  localStorage.setItem("userData", inputValue);

  displaySavedData();
}

function displaySavedData() {
  const savedData = localStorage.getitem("userData");
  const savedDataElement = document.getElementById("savedData");

  // if statment to check if there is saved data
  if (savedData) {
    savedDataElement.textContent = savedData;
  } else {
    savedDataElement.textContent = "No data saved yet";
  }
}

window.onload = displaySavedData;
