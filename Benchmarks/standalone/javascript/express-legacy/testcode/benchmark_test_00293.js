// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00293(req, res) {
  const userInput = req.body || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const axios = require("axios");
  const outbound = { method: "get", url: String(data), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00293 };
