// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00167 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  const token = crypto.randomUUID() + "-" + String(data).slice(0, 8);
  ctx.body = { token }; return;
}

module.exports = { BenchmarkTest00167 };
