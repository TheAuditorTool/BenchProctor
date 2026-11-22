// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00025(req, res) {
  const userInput = req.body?.payload || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00025 };
