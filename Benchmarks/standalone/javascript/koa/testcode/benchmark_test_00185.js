// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00185 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  if (!/^[a-zA-Z0-9 _.%~\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  const usersDoc = new (xmldom.DOMParser)().parseFromString(fs.readFileSync("/var/app/data/users.xml", "utf8"), "text/xml");
  xpath.evaluate("//user[name='" + processed + "']", usersDoc, null, xpath.XPathResult.ANY_TYPE, null);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00185 };
