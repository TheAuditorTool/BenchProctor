// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00073(req, res) {
  const userInput = req.params.id || "";
  const recordCount = parseInt(String(userInput), 10);
  const table = new ArrayBuffer((recordCount * 64) >>> 0);
  res.json({ allocated: table.byteLength }); return;
}

module.exports = { BenchmarkTest00073 };
