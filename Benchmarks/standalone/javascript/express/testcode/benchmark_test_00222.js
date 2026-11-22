// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00222(req, res) {
  const userInput = req.body?.variables?.input || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const quantity = parseInt(String(data), 10);
  const totalCents = Math.imul(quantity, 1999);
  res.json({ quantity, totalCents }); return;
}

module.exports = { BenchmarkTest00222 };
