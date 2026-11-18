// SPDX-License-Identifier: Apache-2.0
const http = require("http");

const BenchmarkTest00261 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = Buffer.from(userInput, "base64").toString();
  http.get(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00261 };
