// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00241 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const { parseXmlString } = require("libxmljs2");
  parseXmlString(String(data), { noent: false, dtdload: false, nonet: true });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00241 };
