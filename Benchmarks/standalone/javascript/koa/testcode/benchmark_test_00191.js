// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00191 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const digest = await crypto.subtle.digest("SHA-256", Buffer.from(String(data)));
  ctx.body = { fingerprint: Buffer.from(digest).toString("hex") }; return;
}

module.exports = { BenchmarkTest00191 };
