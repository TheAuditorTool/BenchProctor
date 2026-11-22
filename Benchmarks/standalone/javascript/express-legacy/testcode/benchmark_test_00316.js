// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function BenchmarkTest00316(req, res) {
  const userInput = (await require("./shared").mq.receive("app-events"));
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  net.connect(80, new URL(String(data)).hostname);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00316 };
