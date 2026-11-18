// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00379(req, res) {
  const userInput = req.body || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  req.session.data = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00379 };
