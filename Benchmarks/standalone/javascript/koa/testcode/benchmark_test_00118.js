// SPDX-License-Identifier: Apache-2.0
const vm = require("node:vm");

const BenchmarkTest00118 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  vm.runInNewContext(String(processed), { Math });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00118 };
