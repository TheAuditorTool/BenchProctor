// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00258 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = Buffer.from(userInput, "hex").toString();
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  ctx.session.data = String(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00258 };
