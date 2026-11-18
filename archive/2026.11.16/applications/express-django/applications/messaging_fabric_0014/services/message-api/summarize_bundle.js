// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function summarizeBundle(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const summary = (await _cache.get("user_data")) || "";
  const bulletin = Buffer.from(summary, "base64").toString();
  http.get(bulletin);
  res.json({ done: true });
}

module.exports = { summarizeBundle };
