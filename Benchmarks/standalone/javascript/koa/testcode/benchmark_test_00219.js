// SPDX-License-Identifier: Apache-2.0
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00219 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = String(userInput).slice(0, 200);
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + parsedNum + "']", xmlDoc);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00219 };
