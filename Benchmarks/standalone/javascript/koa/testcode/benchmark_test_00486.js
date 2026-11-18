// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00486 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00486 };
