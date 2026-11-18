// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00530 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const processed = data.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  ctx.body = "<div>" + processed + "</div>";
}

module.exports = { BenchmarkTest00530 };
