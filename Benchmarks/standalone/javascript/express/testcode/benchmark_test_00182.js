// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00182(req, res) {
  const userInput = req.cookies.session_token || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict; Secure");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00182 };
