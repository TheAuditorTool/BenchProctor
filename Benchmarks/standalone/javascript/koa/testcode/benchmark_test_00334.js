// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00334 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  ctx.session.data = String(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00334 };
