// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00187 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const data = `${userInput}`;
  ctx.session.data = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00187 };
