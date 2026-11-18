// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00351(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  res.json({ token });
}

module.exports = { BenchmarkTest00351 };
