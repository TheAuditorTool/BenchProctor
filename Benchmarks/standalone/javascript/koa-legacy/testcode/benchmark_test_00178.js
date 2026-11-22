// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

const BenchmarkTest00178 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  await libxmljs.parseXmlAsync(String(data), { replaceEntities: false });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00178 };
