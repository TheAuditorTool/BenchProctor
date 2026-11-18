// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00379 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = userInput != null ? userInput : '';
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00379 };
