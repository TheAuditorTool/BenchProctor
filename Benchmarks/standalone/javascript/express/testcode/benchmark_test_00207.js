// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00207(req, res) {
  const userInput = req.body || "";
  const data = `${userInput}`;
  const quantity = parseInt(String(data), 10);
  const totalCents = Math.imul(quantity, 1999);
  res.json({ quantity, totalCents }); return;
}

module.exports = { BenchmarkTest00207 };
