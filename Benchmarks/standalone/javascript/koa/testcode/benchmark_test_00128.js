// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00128 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = Buffer.from(userInput, "base64").toString();
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00128 };
