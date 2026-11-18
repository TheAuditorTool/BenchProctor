// SPDX-License-Identifier: Apache-2.0
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00239 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  if (!/^[a-zA-Z0-9 _.%~\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + processed + "']", xmlDoc);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00239 };
