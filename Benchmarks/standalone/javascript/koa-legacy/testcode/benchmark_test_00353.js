// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00353 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  const targetUrl = data;
  const axios = require("axios");
  const outbound = { method: "get", url: String(targetUrl), timeout: 5000 };
  await axios.request(outbound);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00353 };
