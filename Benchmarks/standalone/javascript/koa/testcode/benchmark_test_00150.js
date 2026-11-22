// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00150 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = Buffer.from(userInput, "utf-8").toString();
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00150 };
