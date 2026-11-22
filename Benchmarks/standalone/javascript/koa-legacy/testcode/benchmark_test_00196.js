// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00196 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  ctx.session.data = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00196 };
