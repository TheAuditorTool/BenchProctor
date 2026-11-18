// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00349 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  ctx.session.data = String(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00349 };
