// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00320 = async (ctx) => {
  const userInput = ctx.request.body || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00320 };
