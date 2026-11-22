// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00227(req, res) {
  const userInput = req.headers["user-agent"] || "";
  res.cookie("session", userInput, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00227 };
