// SPDX-License-Identifier: Apache-2.0
const http = require("http");

const BenchmarkTest00257 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  http.get(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00257 };
