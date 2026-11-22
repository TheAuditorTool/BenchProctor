// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00058 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  new Function("return (" + String(parsedNum) + ");")();
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00058 };
