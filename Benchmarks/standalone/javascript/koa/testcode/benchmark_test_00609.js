// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00609 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00609 };
