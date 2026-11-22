// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00055 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const data = `${userInput}`;
  const digest = await crypto.subtle.digest("SHA-256", Buffer.from(String(data)));
  ctx.body = { fingerprint: Buffer.from(digest).toString("hex") }; return;
}

module.exports = { BenchmarkTest00055 };
