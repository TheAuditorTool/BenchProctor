// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00267 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const lodash = require("lodash");
  const token = lodash.random(1e11, 1e12 - 1).toString(36) + "-" + String(data).slice(0, 8);
  ctx.body = { token }; return;
}

module.exports = { BenchmarkTest00267 };
