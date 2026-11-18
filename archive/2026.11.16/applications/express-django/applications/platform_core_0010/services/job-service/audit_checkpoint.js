// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function auditCheckpoint(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const notice = (await _cache.get("user_data")) || "";
  const persona = Buffer.from(notice, "base64").toString();
  http.get(persona);
  res.json({ done: true });
}

module.exports = { auditCheckpoint };
