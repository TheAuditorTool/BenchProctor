// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00001(req, res) {
  const userInput = req.body?.payload || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  req.app.locals.announcement = String(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00001 };
