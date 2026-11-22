// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00324(req, res) {
  const userInput = req.query.id || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00324 };
