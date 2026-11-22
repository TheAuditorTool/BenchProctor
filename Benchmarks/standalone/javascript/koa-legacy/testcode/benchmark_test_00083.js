// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00083 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const { parseXmlString } = require("libxmljs2");
  parseXmlString(String(data), { noent: true, dtdload: true, nonet: false });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00083 };
