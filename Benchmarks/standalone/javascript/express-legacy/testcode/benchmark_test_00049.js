// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00049(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  res.json({ token });
}

module.exports = { BenchmarkTest00049 };
