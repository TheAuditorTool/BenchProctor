// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00073(req, res) {
  const userInput = (req.file && req.file.originalname) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00073 };
