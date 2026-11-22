// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00278 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  const usersDoc = new (xmldom.DOMParser)().parseFromString(fs.readFileSync("/var/app/data/users.xml", "utf8"), "text/xml");
  xpath.parse("//user[name='" + processed + "']").select({ node: usersDoc });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00278 };
