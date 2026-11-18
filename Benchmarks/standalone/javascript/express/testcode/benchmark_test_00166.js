// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00166(req, res) {
  const userInput = req.body || "";
  const data = String(userInput).slice(0, 200);
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(data)) { res.status(403).json({error:"forbidden"}); return; }
  const checkedPath = "/var/app/data/" + data;
  const fileContent = fs.readFileSync(checkedPath, "utf8");
  res.send(fileContent);
}

module.exports = { BenchmarkTest00166 };
