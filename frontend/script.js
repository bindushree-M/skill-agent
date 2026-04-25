async function submitData() {
  const skill = document.getElementById("skill").value;
  const level = document.getElementById("level").value;
  const goal = document.getElementById("goal").value;

  const response = await fetch("http://127.0.0.1:5000/assess", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ skill, level, goal })
  });

  const data = await response.json();

  document.getElementById("output").innerText =
    "Score: " + data.score + "\n" +
    "Goal: " + data.goal + "\n" +
    "Roadmap:\n- " + data.roadmap.join("\n- ");
}