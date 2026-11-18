// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function BenchmarkTest00465(req, res) {
  const userInput = req.cookies.session_token || "";
  const [data] = String(userInput).split(',');
  http.get(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00465 };
