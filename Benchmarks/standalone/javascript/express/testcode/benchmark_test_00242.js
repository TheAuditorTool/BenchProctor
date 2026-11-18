// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00242(req, res) {
  const userInput = req.cookies.session_token || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00242 };
