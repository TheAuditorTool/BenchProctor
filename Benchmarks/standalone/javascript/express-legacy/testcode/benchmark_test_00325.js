// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00325(req, res) {
  const userInput = req.body || "";
  new Function("return (" + String(userInput) + ");")();
  res.json({ done: true });
}

module.exports = { BenchmarkTest00325 };
