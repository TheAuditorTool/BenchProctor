// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00370(req, res) {
  const userInput = req.headers.origin || "";
  res.cookie("session", userInput, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00370 };
