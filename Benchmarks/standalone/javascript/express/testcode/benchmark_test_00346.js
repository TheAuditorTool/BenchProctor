// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00346(req, res) {
  const userInput = req.body.multipart_field || "";
  res.cookie("session", userInput, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00346 };
