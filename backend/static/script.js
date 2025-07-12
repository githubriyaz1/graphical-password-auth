const BASE_URL = "https://graphical-password-auth-from-riyaz.onrender.com";

async function register() {
  const username = document.getElementById("username").value;
  if (!username || clickPoints.length < 3) {
    showStatus("Enter username and click at least 3 points.");
    return;
  }

  const res = await fetch(`${BASE_URL}/register`, {
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

  const res = await fetch(`${BASE_URL}/login`, {
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
