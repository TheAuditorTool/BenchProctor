// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00356 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  ctx.body = { token };
}

module.exports = { BenchmarkTest00356 };
