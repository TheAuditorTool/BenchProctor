// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00563 = async (ctx) => {
  const userInput = ctx.request.body || "";
  libxmljs.parseXml(userInput, { noent: true, dtdload: true, nonet: false });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00563 };
