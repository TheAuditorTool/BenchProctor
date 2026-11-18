// SPDX-License-Identifier: Apache-2.0
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

async function BenchmarkTest00651(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const data = String(userInput).slice(0, 200);
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + data + "']", xmlDoc);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00651 };
