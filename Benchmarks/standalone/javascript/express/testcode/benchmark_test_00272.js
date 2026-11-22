// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00272(req, res) {
  const userInput = req.query.id || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00272 };
