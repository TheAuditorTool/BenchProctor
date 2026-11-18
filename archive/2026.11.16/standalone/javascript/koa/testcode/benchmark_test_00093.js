// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00093 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = userInput != null ? userInput : '';
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  ctx.body = { token };
}

module.exports = { BenchmarkTest00093 };
