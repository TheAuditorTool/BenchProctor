// SPDX-License-Identifier: Apache-2.0
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

async function BenchmarkTest00511(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const data = `${userInput}`;
  if (!/^[a-zA-Z0-9 _.%~\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + processed + "']", xmlDoc);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00511 };
