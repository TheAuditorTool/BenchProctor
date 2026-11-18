// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00319(req, res) {
  const userInput = req.headers.authorization || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  req.session.data = String(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00319 };
