// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function BenchmarkTest00297(req, res) {
  const userInput = req.body || "";
  const data = String(userInput).replace(/\u0000/g, "");
  http.get(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00297 };
