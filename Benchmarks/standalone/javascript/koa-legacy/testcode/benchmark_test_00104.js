// SPDX-License-Identifier: Apache-2.0
const vm = require("node:vm");

const BenchmarkTest00104 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  vm.runInNewContext(String(parsedNum), { Math });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00104 };
