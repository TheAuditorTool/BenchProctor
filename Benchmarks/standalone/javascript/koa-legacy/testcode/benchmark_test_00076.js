// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00076 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const digest = await crypto.subtle.digest("SHA-1", Buffer.from(String(data)));
  ctx.body = { fingerprint: Buffer.from(digest).toString("hex") }; return;
}

module.exports = { BenchmarkTest00076 };
