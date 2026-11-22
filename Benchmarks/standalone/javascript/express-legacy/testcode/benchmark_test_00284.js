// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00284(req, res) {
  const userInput = req.headers.origin || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  eval(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00284 };
