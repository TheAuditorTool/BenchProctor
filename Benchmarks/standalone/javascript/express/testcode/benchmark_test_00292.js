// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00292(req, res) {
  const userInput = req.headers.origin || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  if (!/^[a-zA-Z0-9 _.\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  Object.assign(req.session, { data: String(processed), expiresAt: Date.now() + 900000 });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00292 };
