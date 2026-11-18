// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00517(req, res) {
  const userInput = (req.file && req.file.originalname) || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  eval(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00517 };
