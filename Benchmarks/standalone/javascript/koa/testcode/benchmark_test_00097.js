// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00097 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  ctx.redirect(userInput);
}

module.exports = { BenchmarkTest00097 };
