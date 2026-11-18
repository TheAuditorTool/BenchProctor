// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const nodeUtil = require("util");
const libxmljs = require("libxmljs");

async function BenchmarkTest00076(req, res) {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const data = nodeUtil.format("%s", userInput);
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00076 };
