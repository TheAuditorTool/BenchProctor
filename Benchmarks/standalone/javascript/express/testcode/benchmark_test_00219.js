// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function BenchmarkTest00219(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  http.get(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00219 };
