// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00347(req, res) {
  const userInput = req.cookies.session_token || "";
  const data = `${userInput}`;
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00347 };
