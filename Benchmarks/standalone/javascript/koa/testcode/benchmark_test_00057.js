// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00057 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00057 };
