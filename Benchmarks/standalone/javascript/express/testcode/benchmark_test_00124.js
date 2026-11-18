// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00124(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  req.session.data = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00124 };
