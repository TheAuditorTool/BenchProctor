// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00462(req, res) {
  const userInput = req.params.id || "";
  const [data] = String(userInput).split(',');
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00462 };
