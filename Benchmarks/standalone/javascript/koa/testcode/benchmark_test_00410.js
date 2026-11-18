// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00410 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = String(userInput).slice(0, 200);
  ctx.session.data = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00410 };
