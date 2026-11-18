// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const nodeSerialize = require("node-serialize");

const BenchmarkTest00248 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const data = nodeUtil.format("%s", userInput);
  nodeSerialize.unserialize(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00248 };
