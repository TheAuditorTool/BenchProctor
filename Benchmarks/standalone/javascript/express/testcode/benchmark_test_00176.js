// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00176(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  eval(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00176 };
