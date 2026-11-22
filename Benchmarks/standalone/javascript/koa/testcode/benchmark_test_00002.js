// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00002 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  const domain = String(data).match(/@([A-Za-z0-9.-]+)$/)[1];
  ctx.body = { domain }; return;
}

module.exports = { BenchmarkTest00002 };
