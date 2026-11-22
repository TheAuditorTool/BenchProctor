// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00341(req, res) {
  const userInput = req.headers.referer || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const domain = String(data).match(/@([A-Za-z0-9.-]+)$/)[1];
  res.json({ domain }); return;
}

module.exports = { BenchmarkTest00341 };
