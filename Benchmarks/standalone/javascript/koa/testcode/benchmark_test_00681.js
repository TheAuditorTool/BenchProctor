// SPDX-License-Identifier: Apache-2.0
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00681 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + data + "']", xmlDoc);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00681 };
