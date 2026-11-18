// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00046(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  res.redirect(data);
}

module.exports = { BenchmarkTest00046 };
