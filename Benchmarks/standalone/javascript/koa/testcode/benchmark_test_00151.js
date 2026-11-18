// SPDX-License-Identifier: Apache-2.0
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00151 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const data = String(userInput).slice(0, 200);
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + data + "']", xmlDoc);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00151 };
