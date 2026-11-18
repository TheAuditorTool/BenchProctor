// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00372(req, res) {
  const userInput = req.body.payload || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  eval(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00372 };
