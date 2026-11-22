// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00300(req, res) {
  const userInput = req.params.id || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const recordCount = parseInt(String(data), 10);
  const table = new ArrayBuffer((recordCount * 64) >>> 0);
  res.json({ allocated: table.byteLength }); return;
}

module.exports = { BenchmarkTest00300 };
