// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00028(req, res) {
  const userInput = req.headers.authorization || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const recordCount = parseInt(String(data), 10);
  const table = new ArrayBuffer((recordCount * 64) >>> 0);
  res.json({ allocated: table.byteLength }); return;
}

module.exports = { BenchmarkTest00028 };
