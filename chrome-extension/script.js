document.getElementById("generate").addEventListener("click", () => {
  const length = parseInt(document.getElementById("length").value);
  const useSymbols = document.getElementById("symbols").checked;

  let chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  if (useSymbols) chars += "!@#$%^&*()_+-=[]{}|;:,.<>?/";

  let pw = "";
  for (let i = 0; i < length; i++) {
    pw += chars[Math.floor(Math.random() * chars.length)];
  }

  document.getElementById("output").value = pw;
});
