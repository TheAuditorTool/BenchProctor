// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00096 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = nodeUtil.format("%s", userInput);
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  ctx.session.data = String(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00096 };
