// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00706(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const data = userInput != null ? userInput : '';
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  res.send("<div>" + processed + "</div>");
}

module.exports = { BenchmarkTest00706 };
