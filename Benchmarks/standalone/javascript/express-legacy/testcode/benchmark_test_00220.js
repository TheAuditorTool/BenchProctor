// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00220(req, res) {
  const userInput = req.cookies.session_token || "";
  const [data] = String(userInput).split(',');
  res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00220 };
