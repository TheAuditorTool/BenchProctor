// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00075(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  eval(userInput);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00075 };
