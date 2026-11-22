// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00139 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00139 };
