// SPDX-License-Identifier: Apache-2.0
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00368 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  const data = userInput != null ? userInput : '';
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + data + "']", xmlDoc);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00368 };
