// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const libxmljs = require("libxmljs");

const BenchmarkTest00150 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = nodeUtil.format("%s", userInput);
  await libxmljs.parseXmlAsync(String(data), { replaceEntities: true });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00150 };
