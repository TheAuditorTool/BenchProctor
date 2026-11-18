// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00685 = async (ctx) => {
  const userInput = ctx.request.body || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  eval(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00685 };
