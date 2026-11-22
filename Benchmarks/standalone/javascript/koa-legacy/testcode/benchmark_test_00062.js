// SPDX-License-Identifier: Apache-2.0
const http = require("http");

const BenchmarkTest00062 = async (ctx) => {
  const userInput = (await require("./shared").mq.receive("app-events"));
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  http.get(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00062 };
