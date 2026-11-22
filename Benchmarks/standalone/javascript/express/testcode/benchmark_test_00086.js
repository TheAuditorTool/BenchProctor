// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00086(req, res) {
  const userInput = req.params.id || "";
  req.session.data = String(userInput);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00086 };
