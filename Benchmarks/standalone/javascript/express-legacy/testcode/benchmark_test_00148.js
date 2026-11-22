// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00148(req, res) {
  const userInput = req.headers.referer || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  res.send("<div>" + processed + "</div>");
}

module.exports = { BenchmarkTest00148 };
