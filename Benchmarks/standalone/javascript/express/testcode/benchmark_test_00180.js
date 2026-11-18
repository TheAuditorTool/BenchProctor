// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00180(req, res) {
  const userInput = req.body.field || "";
  const data = userInput != null ? userInput : '';
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00180 };
