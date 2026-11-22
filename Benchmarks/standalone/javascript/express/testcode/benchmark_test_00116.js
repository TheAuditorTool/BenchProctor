// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const fs = require("fs");
const path = require("path");

async function BenchmarkTest00116(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const checkedPath = "/var/app/data/" + path.basename(data);
  fs.unlinkSync(checkedPath);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00116 };
