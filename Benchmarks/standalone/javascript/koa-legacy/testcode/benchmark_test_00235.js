// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00235 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const usersDoc = new (xmldom.DOMParser)().parseFromString(fs.readFileSync("/var/app/data/users.xml", "utf8"), "text/xml");
  xpath.parse("//user[name='" + data + "']").select({ node: usersDoc });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00235 };
