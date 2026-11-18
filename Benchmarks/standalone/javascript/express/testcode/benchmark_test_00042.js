// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00042(req, res) {
  const userInput = req.body || "";
  req.session.data = String(userInput);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00042 };
