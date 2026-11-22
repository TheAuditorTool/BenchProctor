// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00345 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const data = String(userInput).slice(0, 200);
  const token = crypto.randomUUID() + "-" + String(data).slice(0, 8);
  ctx.body = { token }; return;
}

module.exports = { BenchmarkTest00345 };
