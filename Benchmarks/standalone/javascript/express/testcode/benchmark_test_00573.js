// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00573(req, res) {
  const userInput = req.cookies.session_token || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const processed = data.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.send("<div>" + processed + "</div>");
}

module.exports = { BenchmarkTest00573 };
