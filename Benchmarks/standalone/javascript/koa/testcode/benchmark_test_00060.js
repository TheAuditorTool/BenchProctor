// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00060 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = userInput != null ? userInput : '';
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00060 };
