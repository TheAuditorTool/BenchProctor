// SPDX-License-Identifier: Apache-2.0
const http = require("http");

const BenchmarkTest00203 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  http.get(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00203 };
