// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00062 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00062 };
