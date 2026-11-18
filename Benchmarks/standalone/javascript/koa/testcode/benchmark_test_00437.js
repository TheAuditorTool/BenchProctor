// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00437 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00437 };
