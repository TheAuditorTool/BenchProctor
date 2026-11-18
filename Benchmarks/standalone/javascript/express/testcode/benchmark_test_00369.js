// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00369(req, res) {
  const userInput = (req.file && req.file.originalname) || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  req.session.data = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00369 };
