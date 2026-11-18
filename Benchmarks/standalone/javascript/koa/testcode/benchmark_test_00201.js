// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

const BenchmarkTest00201 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = String(userInput).slice(0, 200);
  nodeSerialize.unserialize(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00201 };
