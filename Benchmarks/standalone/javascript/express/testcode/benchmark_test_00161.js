// SPDX-License-Identifier: Apache-2.0
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

async function BenchmarkTest00161(req, res) {
  const userInput = (req.file && req.file.originalname) || "";
  const data = userInput != null ? userInput : '';
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + parsedNum + "']", xmlDoc);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00161 };
