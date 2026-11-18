// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00052(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  res.json({ allocated: buf.length }); return;
}

module.exports = { BenchmarkTest00052 };
