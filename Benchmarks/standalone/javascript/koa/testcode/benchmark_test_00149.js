// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00149 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00149 };
