// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00262(req, res) {
  const userInput = req.params.id || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  return res.status(302).set("Location", String(data)).end();
}

module.exports = { BenchmarkTest00262 };
