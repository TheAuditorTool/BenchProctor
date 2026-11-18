// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00475 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = String(userInput).slice(0, 200);
  ctx.session.data = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00475 };
