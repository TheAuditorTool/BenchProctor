// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00043(req, res) {
  const userInput = req.body.field || "";
  res.cookie("session", userInput, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00043 };
