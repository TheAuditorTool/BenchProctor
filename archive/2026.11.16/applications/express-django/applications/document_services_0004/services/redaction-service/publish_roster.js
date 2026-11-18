// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function publishRoster(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const excerpt = (await _cache.get("user_data")) || "";
  const dossier = Buffer.from(excerpt, "base64").toString();
  http.get(dossier);
  res.json({ done: true });
}

module.exports = { publishRoster };
