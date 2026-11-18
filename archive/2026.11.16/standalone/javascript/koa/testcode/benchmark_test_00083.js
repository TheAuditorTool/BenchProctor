// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00083 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00083 };
