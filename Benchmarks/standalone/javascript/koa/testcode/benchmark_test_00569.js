// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00569 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00569 };
