// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00490(req, res) {
  const userInput = req.query.id || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00490 };
