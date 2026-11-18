// SPDX-License-Identifier: Apache-2.0
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00688 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const processed = ["true", "1", "yes", "on"].includes(String(userInput).toLowerCase()) ? "true" : "false";
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + processed + "']", xmlDoc);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00688 };
