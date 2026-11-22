// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00136 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = String(userInput).slice(0, 200);
  const lodash = require("lodash");
  const token = lodash.random(1e11, 1e12 - 1).toString(36) + "-" + String(data).slice(0, 8);
  ctx.body = { token }; return;
}

module.exports = { BenchmarkTest00136 };
