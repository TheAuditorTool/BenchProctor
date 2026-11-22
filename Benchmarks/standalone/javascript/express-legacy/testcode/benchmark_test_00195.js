// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00195(req, res) {
  const userInput = req.body.payload || "";
  const data = `${userInput}`;
  res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict; Secure");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00195 };
