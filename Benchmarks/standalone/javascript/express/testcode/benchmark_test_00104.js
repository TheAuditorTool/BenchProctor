// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00104(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00104 };
