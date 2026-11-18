// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00508(req, res) {
  const userInput = req.body.payload || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  eval(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00508 };
