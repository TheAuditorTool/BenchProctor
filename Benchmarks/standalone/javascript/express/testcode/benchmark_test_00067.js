// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00067(req, res) {
  const userInput = req.query.id || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  eval(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00067 };
