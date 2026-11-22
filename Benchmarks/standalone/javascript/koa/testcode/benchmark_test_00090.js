// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00090 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = String(userInput).slice(0, 200);
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00090 };
