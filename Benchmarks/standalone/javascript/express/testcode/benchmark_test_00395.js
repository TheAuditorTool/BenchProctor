// SPDX-License-Identifier: Apache-2.0
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

async function BenchmarkTest00395(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const data = String(userInput).slice(0, 200);
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + processed + "']", xmlDoc);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00395 };
