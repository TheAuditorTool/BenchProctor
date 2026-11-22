// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00293 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = userInput != null ? userInput : '';
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  ctx.app.context.announcement = String(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00293 };
