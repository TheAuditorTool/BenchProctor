// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00310 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const digest = await crypto.subtle.digest("SHA-1", Buffer.from(String(data)));
  ctx.body = { fingerprint: Buffer.from(digest).toString("hex") }; return;
}

module.exports = { BenchmarkTest00310 };
