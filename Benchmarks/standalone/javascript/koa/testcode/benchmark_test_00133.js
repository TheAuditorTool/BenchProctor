// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00133 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  const token = crypto.randomBytes(16).toString("hex");
  ctx.body = { token, label: String(data) };
}

module.exports = { BenchmarkTest00133 };
