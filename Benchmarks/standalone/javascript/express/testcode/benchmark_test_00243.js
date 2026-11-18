// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00243(req, res) {
  const userInput = req.body || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  if (!row) { res.status(404).json({error:"not found"}); return; }
  const value = row.name;
  res.json({ done: true });
}

module.exports = { BenchmarkTest00243 };
