// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00386(req, res) {
  const userInput = req.body.payload || "";
  res.cookie("session", userInput, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00386 };
