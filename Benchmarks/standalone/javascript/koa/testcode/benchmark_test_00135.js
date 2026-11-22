// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00135 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const usersDoc = new (xmldom.DOMParser)().parseFromString(fs.readFileSync("/var/app/data/users.xml", "utf8"), "text/xml");
  xpath.parse("//user[name='" + userInput + "']").select({ node: usersDoc });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00135 };
