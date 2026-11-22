// SPDX-License-Identifier: Apache-2.0
const net = require("net");

const BenchmarkTest00101 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  net.connect(80, new URL(String(data)).hostname);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00101 };
