// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00267(req, res) {
  const userInput = req.body?.variables?.input || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  const value = row.name;
  res.json({ done: true });
}

module.exports = { BenchmarkTest00267 };
