// SPDX-License-Identifier: Apache-2.0
const http = require("http");

const BenchmarkTest00234 = async (ctx) => {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const userInput = (await _cache.get("user_data")) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  http.get(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00234 };
