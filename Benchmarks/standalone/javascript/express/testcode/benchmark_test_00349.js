// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00349(req, res) {
  const userInput = req.body.payload || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  const value = row.name;
  res.json({ done: true });
}

module.exports = { BenchmarkTest00349 };
