// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00186(req, res) {
  const userInput = req.body || "";
  res.cookie("session", userInput, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00186 };
