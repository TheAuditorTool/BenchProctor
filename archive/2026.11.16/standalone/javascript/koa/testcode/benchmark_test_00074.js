// SPDX-License-Identifier: Apache-2.0
const http = require("http");
const nodeUtil = require("util");

const BenchmarkTest00074 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const data = nodeUtil.format("%s", userInput);
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { ctx.status = 403; ctx.body = {error:"private or loopback address not allowed"}; return; }
  const _addr = (await require("dns").promises.lookup(_host)).address;
  if (/^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|::[fF]{4}:(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)|[fF][cCdD]|[fF][eE]80:)/.test(_addr)) { ctx.status = 403; ctx.body = {error:"private or loopback address not allowed"}; return; }
  const targetUrl = data;
  http.get(targetUrl);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00074 };
