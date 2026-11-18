// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00221 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const data = String(userInput).replace(/\u0000/g, "");
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00221 };
