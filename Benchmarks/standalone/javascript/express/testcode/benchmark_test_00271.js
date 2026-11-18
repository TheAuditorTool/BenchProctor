// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00271(req, res) {
  const userInput = req.headers.referer || "";
  const data = userInput != null ? userInput : '';
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  res.json({ allocated: buf.length }); return;
}

module.exports = { BenchmarkTest00271 };
