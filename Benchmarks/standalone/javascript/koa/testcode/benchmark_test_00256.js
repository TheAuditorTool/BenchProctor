// SPDX-License-Identifier: Apache-2.0
const net = require("net");

const BenchmarkTest00256 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  net.connect(80, new URL(String(data)).hostname);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00256 };
