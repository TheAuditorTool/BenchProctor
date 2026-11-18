// SPDX-License-Identifier: Apache-2.0
const net = require("net");

const BenchmarkTest00311 = async (ctx) => {
  const userInput = (await require("./shared").mq.receive("app-events"));
  const data = String(userInput).replace(/\u0000/g, "");
  net.connect(80, new URL(String(data)).hostname);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00311 };
