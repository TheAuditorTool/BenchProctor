// SPDX-License-Identifier: Apache-2.0
const http = require("http");

const BenchmarkTest00601 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  http.get(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00601 };
