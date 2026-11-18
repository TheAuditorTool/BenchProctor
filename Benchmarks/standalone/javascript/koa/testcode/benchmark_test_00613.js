// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00613 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00613 };
