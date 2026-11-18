// SPDX-License-Identifier: Apache-2.0
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00408 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const data = `${userInput}`;
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + parsedNum + "']", xmlDoc);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00408 };
