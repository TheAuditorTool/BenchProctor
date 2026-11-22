// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function BenchmarkTest00228(req, res) {
  const userInput = req.headers.authorization || "";
  const data = `${userInput}`;
  const resolved = path.resolve("/var/app/data", data);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const checkedPath = resolved;
  fs.writeFileSync(checkedPath, "data");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00228 };
