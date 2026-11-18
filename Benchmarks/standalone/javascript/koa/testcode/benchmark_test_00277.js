// SPDX-License-Identifier: Apache-2.0
const net = require("net");

const BenchmarkTest00277 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = String(userInput).slice(0, 200);
  net.connect(80, new URL(String(data)).hostname);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00277 };
