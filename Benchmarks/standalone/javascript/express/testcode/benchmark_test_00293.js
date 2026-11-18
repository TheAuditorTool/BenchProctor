// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00293(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  res.json({ token });
}

module.exports = { BenchmarkTest00293 };
