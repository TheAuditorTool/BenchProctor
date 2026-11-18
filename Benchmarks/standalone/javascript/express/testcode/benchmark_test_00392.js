// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00392(req, res) {
  const userInput = req.body.field || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  req.session.data = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00392 };
