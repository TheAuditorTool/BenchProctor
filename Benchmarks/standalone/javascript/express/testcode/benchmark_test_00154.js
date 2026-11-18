// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00154(req, res) {
  const userInput = req.headers.host || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  req.session.data = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00154 };
