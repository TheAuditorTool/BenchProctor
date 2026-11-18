// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function BenchmarkTest00701(req, res) {
  const userInput = req.headers.referer || "";
  const data = String(userInput).slice(0, 200);
  net.connect(80, new URL(String(data)).hostname);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00701 };
