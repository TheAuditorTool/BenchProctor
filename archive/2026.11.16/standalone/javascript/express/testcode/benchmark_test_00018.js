// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00018(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00018 };
