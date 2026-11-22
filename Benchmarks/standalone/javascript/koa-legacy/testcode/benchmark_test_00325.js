// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00325 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  ctx.session.data = String(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00325 };
