// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00068(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  res.json({ allocated: buf.length }); return;
}

module.exports = { BenchmarkTest00068 };
