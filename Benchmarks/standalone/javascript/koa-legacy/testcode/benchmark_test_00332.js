// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00332 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  await libxmljs.parseXmlAsync(String(data), { replaceEntities: true });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00332 };
