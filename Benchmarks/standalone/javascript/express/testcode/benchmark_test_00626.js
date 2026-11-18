// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const nodeSerialize = require("node-serialize");

async function BenchmarkTest00626(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const userInput = (await _cache.get("user_data")) || "";
  const data = nodeUtil.format("%s", userInput);
  nodeSerialize.unserialize(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00626 };
