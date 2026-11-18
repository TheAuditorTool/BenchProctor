// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00695(req, res) {
  const userInput = req.query.id || "";
  const data = userInput != null ? userInput : '';
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  res.json({ token });
}

module.exports = { BenchmarkTest00695 };
