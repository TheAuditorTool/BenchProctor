// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00036(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  const data = `${userInput}`;
  if (!/^[a-zA-Z0-9 _.\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  Object.assign(req.session, { data: String(processed), expiresAt: Date.now() + 900000 });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00036 };
