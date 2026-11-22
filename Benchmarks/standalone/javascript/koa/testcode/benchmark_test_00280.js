// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00280 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  const usersDoc = new (xmldom.DOMParser)().parseFromString(fs.readFileSync("/var/app/data/users.xml", "utf8"), "text/xml");
  xpath.evaluate("//user[name='" + data + "']", usersDoc, null, xpath.XPathResult.ANY_TYPE, null);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00280 };
