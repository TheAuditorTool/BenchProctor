// SPDX-License-Identifier: Apache-2.0

async function composeTemplate(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const heading = (await _cache.get("user_data")) || "";
  const bulletin = Buffer.from(heading, "base64").toString();
  await fetch("http://bounce-handler:8000/record_bounce", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
  res.json({ done: true });
}

module.exports = { composeTemplate };
