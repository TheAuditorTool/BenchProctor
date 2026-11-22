// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

async function BenchmarkTest00121(req, res) {
  const userInput = req.body?.multipart_field || "";
  const [data] = String(userInput).split(',');
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  const usersDoc = new (xmldom.DOMParser)().parseFromString(fs.readFileSync("/var/app/data/users.xml", "utf8"), "text/xml");
  xpath.parse("//user[name='" + parsedNum + "']").select({ node: usersDoc });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00121 };
