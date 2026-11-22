// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00250(req, res) {
  const userInput = req.params.id || "";
  const data = `${userInput}`;
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00250 };
