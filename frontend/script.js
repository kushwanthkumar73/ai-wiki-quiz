function showTab(tab) {
  document.getElementById("generate").classList.add("hidden");
  document.getElementById("history").classList.add("hidden");
  document.getElementById(tab).classList.remove("hidden");
}

// -------------------------
// Generate Quiz
// -------------------------
async function generateQuiz() {
  const url = document.getElementById("wikiUrl").value;
  const container = document.getElementById("quizResult");
  container.innerHTML = "Loading...";

  try {
    const res = await fetch("http://127.0.0.1:8000/generate-quiz", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url })
    });

    const data = await res.json();

    container.innerHTML = `
      <h2>${data.title}</h2>
      <p>${data.summary}</p>
    `;

    data.quiz.quiz.forEach(q => {
      container.innerHTML += `
        <div class="quiz-card">
          <h4>${q.question}</h4>
          <ul>
            ${q.options.map(o => `<li>${o}</li>`).join("")}
          </ul>
          <b>Answer:</b> ${q.answer}<br/>
          <small>${q.explanation}</small>
        </div>
      `;
    });

  } catch (err) {
    container.innerHTML = "❌ Error fetching quiz";
    console.error(err);
  }
}

// -------------------------
// Load History
// -------------------------
async function loadHistory() {
  const list = document.getElementById("historyList");
  list.innerHTML = "Loading...";

  const res = await fetch("http://127.0.0.1:8000/quizzes");
  const data = await res.json();

  list.innerHTML = "";
  data.forEach(q => {
    list.innerHTML += `<li>📝 ${q.title} (ID: ${q.id})</li>`;
  });
}
