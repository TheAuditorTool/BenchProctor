// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00073(req, res) {
  const userInput = req.query.id || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const quantity = parseInt(String(data), 10);
  const totalCents = Math.imul(quantity, 1999);
  res.json({ quantity, totalCents }); return;
}

module.exports = { BenchmarkTest00073 };
