// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00025(req, res) {
  const userInput = req.headers.origin || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  const value = row.name;
  res.json({ done: true });
}

module.exports = { BenchmarkTest00025 };
