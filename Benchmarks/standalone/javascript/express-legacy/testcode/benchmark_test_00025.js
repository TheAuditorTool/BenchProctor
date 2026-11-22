// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00025(req, res) {
  const userInput = req.body.multipart_field || "";
  const data = `${userInput}`;
  res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00025 };
