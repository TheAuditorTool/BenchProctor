// SPDX-License-Identifier: Apache-2.0
const net = require("net");

const BenchmarkTest00212 = async (ctx) => {
  const userInput = (await require("./shared").mq.receive("app-events"));
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  net.connect(80, new URL(String(data)).hostname);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00212 };
