// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

async function BenchmarkTest00281(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const usersDoc = new (xmldom.DOMParser)().parseFromString(fs.readFileSync("/var/app/data/users.xml", "utf8"), "text/xml");
  xpath.evaluate("//user[name='" + data + "']", usersDoc, null, xpath.XPathResult.ANY_TYPE, null);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00281 };
