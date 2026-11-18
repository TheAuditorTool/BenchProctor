// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function BenchmarkTest00120(req, res) {
  const userInput = req.body.field || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  net.connect(80, new URL(String(data)).hostname);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00120 };
