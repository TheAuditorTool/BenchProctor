// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00360(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  const data = `${userInput}`;
  res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00360 };
