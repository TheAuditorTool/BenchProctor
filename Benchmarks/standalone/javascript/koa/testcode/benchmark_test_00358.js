// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00358 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  Object.assign(ctx.session, { data: String(data), expiresAt: Date.now() + 900000 });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00358 };
