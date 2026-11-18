// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function BenchmarkTest00685(req, res) {
  const userInput = req.headers.authorization || "";
  const data = Buffer.from(userInput, "base64").toString();
  http.get(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00685 };
