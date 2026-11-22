// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00240 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  const [data] = String(userInput).split(',');
  const digest = await crypto.subtle.digest("SHA-1", Buffer.from(String(data)));
  ctx.body = { fingerprint: Buffer.from(digest).toString("hex") }; return;
}

module.exports = { BenchmarkTest00240 };
