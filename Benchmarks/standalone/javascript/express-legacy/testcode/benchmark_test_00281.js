// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

async function BenchmarkTest00281(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  const data = `${userInput}`;
  const usersDoc = new (xmldom.DOMParser)().parseFromString(fs.readFileSync("/var/app/data/users.xml", "utf8"), "text/xml");
  xpath.parse("//user[name='" + data + "']").select({ node: usersDoc });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00281 };
