// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function BenchmarkTest00031(req, res) {
  const userInput = req.headers.host || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const resolved = path.resolve("/var/app/data", data);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const checkedPath = resolved;
  fs.unlinkSync(checkedPath);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00031 };
