// SPDX-License-Identifier: Apache-2.0
const http = require("http");

const BenchmarkTest00172 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = Buffer.from(userInput, "hex").toString();
  http.get(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00172 };
