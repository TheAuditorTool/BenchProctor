// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00501(req, res) {
  const userInput = req.body.multipart_field || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  res.json({ allocated: buf.length }); return;
}

module.exports = { BenchmarkTest00501 };
