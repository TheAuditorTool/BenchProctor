// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00445 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  eval(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00445 };
