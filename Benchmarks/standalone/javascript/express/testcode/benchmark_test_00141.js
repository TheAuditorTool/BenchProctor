// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00141(req, res) {
  const userInput = req.body?.field || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const recordCount = parseInt(String(data), 10);
  const table = new ArrayBuffer((recordCount * 64) >>> 0);
  res.json({ allocated: table.byteLength }); return;
}

module.exports = { BenchmarkTest00141 };
