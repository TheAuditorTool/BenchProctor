// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00462 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00462 };
