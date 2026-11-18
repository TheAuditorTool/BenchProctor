// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00153(req, res) {
  const userInput = req.headers.host || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  const value = row.name;
  res.json({ done: true });
}

module.exports = { BenchmarkTest00153 };
