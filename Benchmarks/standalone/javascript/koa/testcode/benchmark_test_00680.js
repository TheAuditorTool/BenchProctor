// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00680 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00680 };
