// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00498 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const data = decodeURIComponent(userInput);
  ctx.session.data = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00498 };
