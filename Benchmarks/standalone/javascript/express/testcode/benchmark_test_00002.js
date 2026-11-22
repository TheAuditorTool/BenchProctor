// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00002(req, res) {
  const userInput = req.body || "";
  const data = String(userInput).slice(0, 200);
  const recordCount = parseInt(String(data), 10);
  const table = new ArrayBuffer((recordCount * 64) >>> 0);
  res.json({ allocated: table.byteLength }); return;
}

module.exports = { BenchmarkTest00002 };
