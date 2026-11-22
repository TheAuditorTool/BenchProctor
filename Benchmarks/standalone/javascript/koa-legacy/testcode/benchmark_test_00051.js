// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00051 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00051 };
