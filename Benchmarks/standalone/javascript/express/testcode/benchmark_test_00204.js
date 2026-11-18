// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00204(req, res) {
  const userInput = req.body || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  eval(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00204 };
