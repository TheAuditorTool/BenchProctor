// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function BenchmarkTest00353(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const userInput = (await _cache.get("user_data")) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  http.get(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00353 };
