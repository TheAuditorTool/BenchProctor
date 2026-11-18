// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00344(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00344 };
