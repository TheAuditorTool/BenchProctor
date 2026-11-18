// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function BenchmarkTest00438(req, res) {
  const userInput = req.cookies.session_token || "";
  const data = Buffer.from(userInput, "hex").toString();
  http.get(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00438 };
