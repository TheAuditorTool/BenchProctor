// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00074(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const data = String(userInput).slice(0, 200);
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  res.json({ allocated: buf.length }); return;
}

module.exports = { BenchmarkTest00074 };
