// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

async function BenchmarkTest00038(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + parsedNum + "']", xmlDoc);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00038 };
