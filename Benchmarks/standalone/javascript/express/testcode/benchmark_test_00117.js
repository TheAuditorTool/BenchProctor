// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function BenchmarkTest00117(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  net.connect(80, new URL(String(data)).hostname);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00117 };
