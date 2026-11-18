// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00100 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  crypto.createHash("sha256").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00100 };
