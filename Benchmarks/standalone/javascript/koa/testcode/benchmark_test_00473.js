// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

const BenchmarkTest00473 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  nodeSerialize.unserialize(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00473 };
