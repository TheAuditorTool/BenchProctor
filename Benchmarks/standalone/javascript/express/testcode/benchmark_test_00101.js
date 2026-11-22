// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const libxmljs = require("libxmljs");

async function BenchmarkTest00101(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  await libxmljs.parseXmlAsync(String(userInput), { replaceEntities: false });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00101 };
