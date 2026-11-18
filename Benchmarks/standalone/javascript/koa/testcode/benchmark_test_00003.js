// SPDX-License-Identifier: Apache-2.0
const net = require("net");

const BenchmarkTest00003 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  net.connect(80, new URL(String(data)).hostname);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00003 };
