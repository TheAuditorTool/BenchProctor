// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

async function BenchmarkTest00092(req, res) {
  const userInput = req.cookies.session_token || "";
  const usersDoc = new (xmldom.DOMParser)().parseFromString(fs.readFileSync("/var/app/data/users.xml", "utf8"), "text/xml");
  xpath.parse("//user[name='" + userInput + "']").select({ node: usersDoc });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00092 };
