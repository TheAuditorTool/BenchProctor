// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const nodeUtil = require("util");

async function BenchmarkTest00112(req, res) {
  const userInput = req.query.id || "";
  const data = nodeUtil.format("%s", userInput);
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  if (!row) { res.status(404).json({error:"not found"}); return; }
  const value = row.name;
  res.json({ done: true });
}

module.exports = { BenchmarkTest00112 };
