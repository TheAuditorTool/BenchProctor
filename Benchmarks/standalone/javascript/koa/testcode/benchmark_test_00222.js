// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00222 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = String(userInput).replace(/\u0000/g, "");
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00222 };
