// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00303 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const digest = await crypto.subtle.digest("SHA-1", Buffer.from(String(data)));
  ctx.body = { fingerprint: Buffer.from(digest).toString("hex") }; return;
}

module.exports = { BenchmarkTest00303 };
