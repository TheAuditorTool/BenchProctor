// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

const BenchmarkTest00200 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  nodeSerialize.unserialize(userInput);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00200 };
