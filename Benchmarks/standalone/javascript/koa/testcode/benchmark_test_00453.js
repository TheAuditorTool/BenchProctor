// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00453 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = Buffer.from(userInput, "utf-8").toString();
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00453 };
