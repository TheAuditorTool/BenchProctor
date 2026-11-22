// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function BenchmarkTest00193(req, res) {
  const userInput = req.body.field || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  net.connect(80, new URL(String(data)).hostname);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00193 };
