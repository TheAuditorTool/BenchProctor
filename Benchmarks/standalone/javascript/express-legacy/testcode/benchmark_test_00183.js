// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00183(req, res) {
  const userInput = req.params.id || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  eval(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00183 };
