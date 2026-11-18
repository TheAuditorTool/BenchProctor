// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00568 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  eval(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00568 };
