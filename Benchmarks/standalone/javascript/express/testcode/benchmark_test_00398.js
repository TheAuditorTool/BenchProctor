// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const path = require("path");
const fs = require("fs");

async function BenchmarkTest00398(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = userInput != null ? userInput : '';
  const resolved = path.resolve("/var/app/data", data);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const checkedPath = resolved;
  fs.unlinkSync(checkedPath);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00398 };
