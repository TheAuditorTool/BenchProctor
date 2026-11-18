// SPDX-License-Identifier: Apache-2.0
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

async function BenchmarkTest00413(req, res) {
  const userInput = req.body.payload || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + data + "']", xmlDoc);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00413 };
