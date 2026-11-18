// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00424 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  eval(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00424 };
