// SPDX-License-Identifier: Apache-2.0
const net = require("net");

const BenchmarkTest00159 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  const targetUrl = data;
  net.connect(80, new URL(String(targetUrl)).hostname);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00159 };
