// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00595 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const [data] = String(userInput).split(',');
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00595 };
