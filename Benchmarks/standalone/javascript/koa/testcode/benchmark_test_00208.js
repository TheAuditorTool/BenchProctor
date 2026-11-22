// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00208 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const data = userInput != null ? userInput : '';
  ctx.set("Location", String(data));
  ctx.status = 302;
}

module.exports = { BenchmarkTest00208 };
