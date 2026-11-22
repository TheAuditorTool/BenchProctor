// SPDX-License-Identifier: Apache-2.0
const http = require("http");

const BenchmarkTest00007 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  const targetUrl = data;
  http.get(targetUrl);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00007 };
