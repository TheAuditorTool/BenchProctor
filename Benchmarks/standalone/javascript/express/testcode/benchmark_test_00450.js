// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00450(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  res.json({ allocated: buf.length }); return;
}

module.exports = { BenchmarkTest00450 };
