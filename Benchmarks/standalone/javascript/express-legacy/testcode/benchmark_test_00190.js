// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00190(req, res) {
  const userInput = req.headers.origin || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const recordCount = parseInt(String(data), 10);
  const table = new ArrayBuffer((recordCount * 64) >>> 0);
  res.json({ allocated: table.byteLength }); return;
}

module.exports = { BenchmarkTest00190 };
