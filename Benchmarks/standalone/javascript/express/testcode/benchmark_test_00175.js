// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00175(req, res) {
  const userInput = process.env.APP_INPUT || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  if (!/^[a-zA-Z0-9 _.\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  Object.assign(req.session, { data: String(processed), expiresAt: Date.now() + 900000 });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00175 };
