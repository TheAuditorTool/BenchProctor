// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00355 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const data = String(userInput).replace(/\u0000/g, "");
  ctx.set("Location", String(data));
  ctx.status = 302;
}

module.exports = { BenchmarkTest00355 };
