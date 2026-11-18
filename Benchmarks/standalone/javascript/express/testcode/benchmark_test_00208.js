// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function BenchmarkTest00208(req, res) {
  const userInput = (await require("./shared").mq.receive("app-events"));
  const data = String(userInput).replace(/\u0000/g, "");
  http.get(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00208 };
