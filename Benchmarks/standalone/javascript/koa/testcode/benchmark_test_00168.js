// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00168 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00168 };
