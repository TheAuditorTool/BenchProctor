// SPDX-License-Identifier: Apache-2.0
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00432 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + processed + "']", xmlDoc);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00432 };
