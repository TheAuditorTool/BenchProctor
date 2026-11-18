// SPDX-License-Identifier: Apache-2.0
const net = require("net");

const BenchmarkTest00038 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  net.connect(80, new URL(String(data)).hostname);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00038 };
