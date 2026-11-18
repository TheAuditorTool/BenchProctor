// SPDX-License-Identifier: Apache-2.0
const net = require("net");

const BenchmarkTest00141 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = `${userInput}`;
  net.connect(80, new URL(String(data)).hostname);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00141 };
