// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00284(req, res) {
  const userInput = req.body?.payload || "";
  eval(userInput);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00284 };
