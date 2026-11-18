// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const nodeSerialize = require("node-serialize");

const BenchmarkTest00419 = async (ctx) => {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const userInput = (await _cache.get("user_data")) || "";
  const data = nodeUtil.format("%s", userInput);
  nodeSerialize.unserialize(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00419 };
