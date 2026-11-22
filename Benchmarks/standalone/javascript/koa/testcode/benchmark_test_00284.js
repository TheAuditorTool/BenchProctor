// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00284 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const data = String(userInput).slice(0, 200);
  eval(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00284 };
