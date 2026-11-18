// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00667(req, res) {
  const userInput = req.body || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00667 };
