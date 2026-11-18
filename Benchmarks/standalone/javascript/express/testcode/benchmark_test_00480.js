// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00480(req, res) {
  const userInput = req.headers.referer || "";
  const data = `${userInput}`;
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  req.session.data = String(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00480 };
