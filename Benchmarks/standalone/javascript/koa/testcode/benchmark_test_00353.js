// SPDX-License-Identifier: Apache-2.0
const http = require("http");

const BenchmarkTest00353 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  let _host = "";
  try { _host = new URL(String(userInput)).hostname; } catch (e) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  const targetUrl = userInput;
  http.get(targetUrl);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00353 };
