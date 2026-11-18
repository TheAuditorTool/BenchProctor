// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const libxmljs = require("libxmljs");

async function BenchmarkTest00654(req, res) {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00654 };
