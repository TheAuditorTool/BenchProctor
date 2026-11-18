// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00103(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  eval(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00103 };
