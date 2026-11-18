// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const nodeUtil = require("util");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

async function BenchmarkTest00060(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = nodeUtil.format("%s", userInput);
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + data + "']", xmlDoc);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00060 };
