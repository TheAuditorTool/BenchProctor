// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

const BenchmarkTest00167 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  nodeSerialize.unserialize(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00167 };
