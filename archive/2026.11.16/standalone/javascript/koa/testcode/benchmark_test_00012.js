// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00012 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const data = String(userInput).replace(/\u0000/g, "");
  ctx.session.data = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00012 };
