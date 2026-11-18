// SPDX-License-Identifier: Apache-2.0
const net = require("net");

const BenchmarkTest00051 = async (ctx) => {
  const userInput = ctx.params.id || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  net.connect(80, new URL(String(data)).hostname);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00051 };
