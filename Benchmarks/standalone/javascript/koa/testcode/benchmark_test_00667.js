// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00667 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  ctx.session.data = String(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00667 };
