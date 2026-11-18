// SPDX-License-Identifier: Apache-2.0
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

async function BenchmarkTest00226(req, res) {
  const userInput = req.body.payload || "";
  const data = `${userInput}`;
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + parsedNum + "']", xmlDoc);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00226 };
