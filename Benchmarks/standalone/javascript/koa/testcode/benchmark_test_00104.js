// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00104 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = Buffer.from(userInput, "utf-8").toString();
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  eval(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00104 };
