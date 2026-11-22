// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function BenchmarkTest00158(req, res) {
  const userInput = (await (await fetch("https://api.partner.example/v1/records")).json()).data || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  http.get(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00158 };
