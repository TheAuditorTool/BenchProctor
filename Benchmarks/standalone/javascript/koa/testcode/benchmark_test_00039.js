// SPDX-License-Identifier: Apache-2.0
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00039 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + data + "']", xmlDoc);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00039 };
