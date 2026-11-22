// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00262 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const { parseXmlString } = require("libxmljs2");
  parseXmlString(String(data), { noent: false, dtdload: false, nonet: true });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00262 };
