// SPDX-License-Identifier: Apache-2.0
const http = require("http");

const BenchmarkTest00101 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  http.get(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00101 };
