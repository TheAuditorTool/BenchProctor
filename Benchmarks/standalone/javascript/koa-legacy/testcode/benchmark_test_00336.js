// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00336 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const domain = String(data).match(/@([A-Za-z0-9.-]+)$/)[1];
  ctx.body = { domain }; return;
}

module.exports = { BenchmarkTest00336 };
