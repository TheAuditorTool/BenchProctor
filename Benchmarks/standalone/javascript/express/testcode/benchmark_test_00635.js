// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00635(req, res) {
  const userInput = req.body || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00635 };
