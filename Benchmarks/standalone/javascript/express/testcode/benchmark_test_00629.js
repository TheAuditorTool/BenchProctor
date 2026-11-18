// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00629(req, res) {
  const userInput = req.body.payload || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00629 };
