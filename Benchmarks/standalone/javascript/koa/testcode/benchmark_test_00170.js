// SPDX-License-Identifier: Apache-2.0
const http = require("http");

const BenchmarkTest00170 = async (ctx) => {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const userInput = (await _cache.get("user_data")) || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  const targetUrl = data;
  http.get(targetUrl);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00170 };
