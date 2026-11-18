// SPDX-License-Identifier: Apache-2.0
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00373 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + data + "']", xmlDoc);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00373 };
