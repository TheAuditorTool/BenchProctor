// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00330 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const data = `${userInput}`;
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00330 };
