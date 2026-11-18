// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00377 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00377 };
