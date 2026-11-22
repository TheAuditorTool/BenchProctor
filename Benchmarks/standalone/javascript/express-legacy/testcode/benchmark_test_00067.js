// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00067(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00067 };
