// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00218 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const token = crypto.randomUUID() + "-" + String(data).slice(0, 8);
  ctx.body = { token }; return;
}

module.exports = { BenchmarkTest00218 };
