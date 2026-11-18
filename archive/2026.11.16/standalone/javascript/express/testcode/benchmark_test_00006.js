// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function BenchmarkTest00006(req, res) {
  const userInput = req.body || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  http.get(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00006 };
