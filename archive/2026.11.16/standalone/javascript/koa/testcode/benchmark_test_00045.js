// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00045 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00045 };
