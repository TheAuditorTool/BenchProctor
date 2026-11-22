// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

const BenchmarkTest00014 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = `${userInput}`;
  nodeSerialize.unserialize(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00014 };
