// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00109(req, res) {
  const userInput = req.body?.multipart_field || "";
  const data = String(userInput).replace(/\u0000/g, "");
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00109 };
