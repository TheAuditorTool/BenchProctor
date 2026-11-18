// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00404(req, res) {
  const userInput = req.params.id || "";
  eval(userInput);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00404 };
