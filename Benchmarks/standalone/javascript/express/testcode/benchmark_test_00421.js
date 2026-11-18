// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function BenchmarkTest00421(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const userInput = (await _cache.get("user_data")) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  net.connect(80, new URL(String(data)).hostname);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00421 };
