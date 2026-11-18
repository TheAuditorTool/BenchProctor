// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00145(req, res) {
  const userInput = req.params.id || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  res.send("<div>" + processed + "</div>");
}

module.exports = { BenchmarkTest00145 };
