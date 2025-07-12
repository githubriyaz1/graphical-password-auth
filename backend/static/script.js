let clickPoints = [];

document.getElementById("loginImage").addEventListener("click", function (e) {
  const rect = e.target.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;

  clickPoints.push({ x: x, y: y });

  const dot = document.createElement("div");
  dot.style.position = "absolute";
  dot.style.left = (x + rect.left) + "px";
  dot.style.top = (y + rect.top) + "px";
  dot.style.width = "8px";
  dot.style.height = "8px";
  dot.style.backgroundColor = "red";
  dot.style.borderRadius = "50%";
  dot.style.zIndex = "10";
  dot.style.position = "fixed";
  document.body.appendChild(dot);
});

async function register() {
  const username = document.getElementById("username").value;
  if (!username || clickPoints.length < 3) {
    showStatus("Enter username and click at least 3 points.");
    return;
  }

  const res = await fetch("http://localhost:5000/register", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, clickPoints }),
  });

  const data = await res.json();
  showStatus(data.message);
}

async function login() {
  const username = document.getElementById("username").value;
  if (!username || clickPoints.length < 3) {
    showStatus("Enter username and click at least 3 points.");
    return;
  }

  const res = await fetch("http://localhost:5000/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, clickPoints }),
  });

  const data = await res.json();
  if (data.success) {
    window.location.href = "dashboard.html";
  } else {
    showStatus(data.message);
  }
}

function showStatus(msg) {
  document.getElementById("statusMsg").textContent = msg;
  clickPoints = [];
}
