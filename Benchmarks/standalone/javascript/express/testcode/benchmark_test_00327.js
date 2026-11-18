// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00327(req, res) {
  const userInput = req.body.field || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00327 };
