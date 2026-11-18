// SPDX-License-Identifier: Apache-2.0
const net = require("net");

const BenchmarkTest00514 = async (ctx) => {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const userInput = (await _cache.get("user_data")) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  net.connect(80, new URL(String(data)).hostname);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00514 };
