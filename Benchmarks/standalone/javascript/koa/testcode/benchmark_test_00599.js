// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00599 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00599 };
