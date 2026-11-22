// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00309 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const token = crypto.randomInt(2 ** 47).toString(36) + crypto.randomInt(2 ** 47).toString(36) + "-" + String(data).slice(0, 8);
  ctx.body = { token }; return;
}

module.exports = { BenchmarkTest00309 };
