// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00020 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00020 };
