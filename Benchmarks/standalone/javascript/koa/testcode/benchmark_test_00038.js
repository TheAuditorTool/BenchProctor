// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00038 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00038 };
