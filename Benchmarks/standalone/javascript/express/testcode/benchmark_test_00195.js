// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00195(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00195 };
