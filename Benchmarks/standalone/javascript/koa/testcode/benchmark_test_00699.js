// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00699 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = decodeURIComponent(userInput);
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00699 };
