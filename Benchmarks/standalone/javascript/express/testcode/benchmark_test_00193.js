// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function BenchmarkTest00193(req, res) {
  const userInput = req.cookies.session_token || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  http.get(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00193 };
