// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const libxmljs = require("libxmljs");

async function BenchmarkTest00163(req, res) {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  await libxmljs.parseXmlAsync(String(data), { replaceEntities: false });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00163 };
