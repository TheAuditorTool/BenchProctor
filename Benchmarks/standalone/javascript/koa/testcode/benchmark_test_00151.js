// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00151 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  const planQuotas = new Map([["basic", { quota: 10 }], ["team", { quota: 50 }], ["enterprise", { quota: 500 }]]);
  const { quota } = planQuotas.get(String(data));
  ctx.body = { quota }; return;
}

module.exports = { BenchmarkTest00151 };
