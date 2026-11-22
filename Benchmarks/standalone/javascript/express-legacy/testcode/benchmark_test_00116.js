// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00116(req, res) {
  const userInput = req.headers.authorization || "";
  const data = Buffer.from(userInput, "base64").toString();
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(data)) { res.status(403).json({error:"forbidden"}); return; }
  const checkedPath = "/var/app/data/" + data;
  fs.writeFileSync(checkedPath, "data");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00116 };
