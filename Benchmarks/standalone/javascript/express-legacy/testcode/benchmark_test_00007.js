// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00007(req, res) {
  const userInput = req.body.multipart_field || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict; Secure");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00007 };
