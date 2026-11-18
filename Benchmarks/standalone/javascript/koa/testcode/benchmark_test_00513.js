// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00513 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const data = `${userInput}`;
  ctx.session.data = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00513 };
