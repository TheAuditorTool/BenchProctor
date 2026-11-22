// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00115(req, res) {
  const userInput = req.body || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict; Secure");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00115 };
