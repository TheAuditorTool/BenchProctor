// SPDX-License-Identifier: Apache-2.0
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00125 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + parsedNum + "']", xmlDoc);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00125 };
