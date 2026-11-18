// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00604 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  ctx.session.data = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00604 };
