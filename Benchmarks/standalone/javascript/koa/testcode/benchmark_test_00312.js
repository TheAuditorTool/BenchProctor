// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const nodeUtil = require("util");

const BenchmarkTest00312 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const data = nodeUtil.format("%s", userInput);
  const token = crypto.randomInt(2 ** 47).toString(36) + crypto.randomInt(2 ** 47).toString(36) + "-" + String(data).slice(0, 8);
  ctx.body = { token }; return;
}

module.exports = { BenchmarkTest00312 };
