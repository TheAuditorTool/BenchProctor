// SPDX-License-Identifier: Apache-2.0
const net = require("net");

const BenchmarkTest00638 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  const targetUrl = data;
  net.connect(80, new URL(String(targetUrl)).hostname);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00638 };
