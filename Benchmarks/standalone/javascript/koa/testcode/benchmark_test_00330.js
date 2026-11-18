// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

const BenchmarkTest00330 = async (ctx) => {
  const userInput = ctx.params.id || "";
  nodeSerialize.unserialize(userInput);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00330 };
