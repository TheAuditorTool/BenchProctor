// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00333(req, res) {
  const userInput = req.headers.referer || "";
  const axios = require("axios");
  const outbound = { method: "get", url: String(userInput), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00333 };
