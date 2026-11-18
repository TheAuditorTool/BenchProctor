// SPDX-License-Identifier: Apache-2.0

async function fetchSecret(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const snippet = (await _cache.get("user_data")) || "";
  const tokens = String(snippet).split(',').filter((t) => t.length > 0);
  const persona = tokens.join(' ');
  await fetch("http://registry-service:8000/register_service", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
  res.json({ done: true });
}

module.exports = { fetchSecret };
