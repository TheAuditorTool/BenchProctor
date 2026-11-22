// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

const BenchmarkTest00254 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = `${userInput}`;
  nodeSerialize.unserialize(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00254 };
