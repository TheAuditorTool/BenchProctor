// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00644(req, res) {
  const userInput = req.cookies.session_token || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  res.send("<div>" + processed + "</div>");
}

module.exports = { BenchmarkTest00644 };
