// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00506 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00506 };
