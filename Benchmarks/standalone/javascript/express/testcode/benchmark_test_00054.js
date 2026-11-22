// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00054(req, res) {
  const userInput = req.headers.host || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  res.location(String(data)).sendStatus(303); return;
}

module.exports = { BenchmarkTest00054 };
