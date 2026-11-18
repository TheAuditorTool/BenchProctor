// SPDX-License-Identifier: Apache-2.0
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00226 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + processed + "']", xmlDoc);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00226 };
