// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00057(req, res) {
  const userInput = req.body.payload || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00057 };
