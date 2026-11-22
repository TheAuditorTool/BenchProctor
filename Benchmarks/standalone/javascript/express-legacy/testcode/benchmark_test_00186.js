// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00186(req, res) {
  const userInput = req.headers.referer || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00186 };
