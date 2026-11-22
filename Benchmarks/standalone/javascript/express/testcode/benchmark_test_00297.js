// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00297(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  const data = `${userInput}`;
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  res.json({ allocated: buf.length }); return;
}

module.exports = { BenchmarkTest00297 };
