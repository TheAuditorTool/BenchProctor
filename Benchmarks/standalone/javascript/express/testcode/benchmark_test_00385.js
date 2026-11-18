// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const libxmljs = require("libxmljs");

async function BenchmarkTest00385(req, res) {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00385 };
