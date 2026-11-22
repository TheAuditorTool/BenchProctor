// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00263 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = userInput != null ? userInput : '';
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00263 };
