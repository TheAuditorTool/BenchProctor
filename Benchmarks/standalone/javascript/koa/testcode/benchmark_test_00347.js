// SPDX-License-Identifier: Apache-2.0
const http = require("http");

const BenchmarkTest00347 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const [data] = String(userInput).split(',');
  http.get(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00347 };
