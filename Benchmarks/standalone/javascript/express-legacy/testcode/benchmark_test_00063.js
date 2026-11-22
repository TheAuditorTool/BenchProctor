// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00063(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  const data = `${userInput}`;
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00063 };
