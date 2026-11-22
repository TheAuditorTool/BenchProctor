// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00109(req, res) {
  const userInput = req.body.multipart_field || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict; Secure");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00109 };
