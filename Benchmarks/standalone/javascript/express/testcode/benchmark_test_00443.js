// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

async function BenchmarkTest00443(req, res) {
  const userInput = req.headers.origin || "";
  const data = nodeUtil.format("%s", userInput);
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + data + "']", xmlDoc);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00443 };
