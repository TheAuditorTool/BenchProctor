// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00243 = async (ctx) => {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const userInput = (await _cache.get("user_data")) || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  await db.query("SELECT * FROM users ORDER BY " + processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00243 };
