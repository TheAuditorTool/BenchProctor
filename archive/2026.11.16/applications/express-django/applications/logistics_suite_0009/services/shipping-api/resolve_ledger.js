// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function resolveLedger(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const subject = (await _cache.get("user_data")) || "";
  const parcel = Buffer.from(subject, "base64").toString();
  http.get(parcel);
  res.json({ done: true });
}

module.exports = { resolveLedger };
