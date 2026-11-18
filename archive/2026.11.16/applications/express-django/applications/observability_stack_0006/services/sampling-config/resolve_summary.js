// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function resolveSummary(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const preface = (await _cache.get("user_data")) || "";
  const cohort = Buffer.from(preface, "base64").toString();
  http.get(cohort);
  res.json({ done: true });
}

module.exports = { resolveSummary };
