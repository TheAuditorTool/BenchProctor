// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00453(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00453 };
