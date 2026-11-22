// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00186 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  eval(userInput);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00186 };
