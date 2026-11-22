// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const libxmljs = require("libxmljs");

const BenchmarkTest00222 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = nodeUtil.format("%s", userInput);
  await libxmljs.parseXmlAsync(String(data), { replaceEntities: false });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00222 };
