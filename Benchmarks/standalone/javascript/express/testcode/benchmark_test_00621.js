// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00621(req, res) {
  const userInput = req.params.id || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  eval(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00621 };
