// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00128(req, res) {
  const userInput = req.query.id || "";
  const data = userInput != null ? userInput : '';
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(data)) { res.status(403).json({error:"forbidden"}); return; }
  const checkedPath = "/var/app/data/" + data;
  fs.writeFileSync(checkedPath, "data");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00128 };
