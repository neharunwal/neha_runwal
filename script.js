const themes = ["midnight", "ember", "jade", "plum"];
const themeCookieName = "neha-career-theme";

function getCookie(name) {
  const prefix = `${name}=`;
  const value = document.cookie
    .split("; ")
    .find((item) => item.startsWith(prefix))
    ?.slice(prefix.length);

  return value ? decodeURIComponent(value) : null;
}

function setCookie(name, value, days = 365) {
  const maxAge = days * 24 * 60 * 60;
  document.cookie = `${name}=${encodeURIComponent(value)}; path=/; max-age=${maxAge}; SameSite=Lax`;
}

function applyTheme(theme) {
  const safeTheme = themes.includes(theme) ? theme : themes[0];
  document.body.dataset.theme = safeTheme;
  setCookie(themeCookieName, safeTheme);
}

document.getElementById("themeCycle").addEventListener("click", () => {
  const current = document.body.dataset.theme || themes[0];
  const next = themes[(themes.indexOf(current) + 1) % themes.length];
  applyTheme(next);
});

applyTheme(getCookie(themeCookieName) || "midnight");
