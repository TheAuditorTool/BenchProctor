// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00497 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  ctx.body = "<div>" + processed + "</div>";
}

module.exports = { BenchmarkTest00497 };
