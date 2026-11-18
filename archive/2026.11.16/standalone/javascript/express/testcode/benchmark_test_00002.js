// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00002(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const data = `${userInput}`;
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00002 };
