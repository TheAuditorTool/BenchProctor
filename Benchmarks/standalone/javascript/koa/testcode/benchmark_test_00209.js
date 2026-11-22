// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00209 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  await libxmljs.parseXmlAsync(String(data), { replaceEntities: true });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00209 };
