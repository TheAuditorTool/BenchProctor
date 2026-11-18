// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00396(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  res.json({ token });
}

module.exports = { BenchmarkTest00396 };
