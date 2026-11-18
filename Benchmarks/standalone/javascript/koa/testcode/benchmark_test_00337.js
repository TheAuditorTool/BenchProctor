// SPDX-License-Identifier: Apache-2.0
const http = require("http");

const BenchmarkTest00337 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = String(userInput).replace(/\u0000/g, "");
  http.get(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00337 };
