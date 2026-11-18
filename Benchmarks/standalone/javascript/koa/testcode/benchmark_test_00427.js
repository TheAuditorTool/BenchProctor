// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00427 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  libxmljs.parseXml(userInput, { noent: false, dtdload: false, nonet: true });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00427 };
