// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00129(req, res) {
  const userInput = req.body?.variables?.input || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const axios = require("axios");
  const outbound = { method: "get", url: String(data), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00129 };
