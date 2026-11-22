// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const libxmljs = require("libxmljs");

async function BenchmarkTest00203(req, res) {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  await libxmljs.parseXmlAsync(String(data), { replaceEntities: true });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00203 };
