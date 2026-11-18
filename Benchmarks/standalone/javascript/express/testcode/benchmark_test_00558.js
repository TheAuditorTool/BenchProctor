// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00558(req, res) {
  const userInput = req.headers.authorization || "";
  const data = Buffer.from(userInput, "hex").toString();
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  const value = row.name;
  res.json({ done: true });
}

module.exports = { BenchmarkTest00558 };
