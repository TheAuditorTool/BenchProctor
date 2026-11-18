// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00210 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const data = userInput != null ? userInput : '';
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00210 };
