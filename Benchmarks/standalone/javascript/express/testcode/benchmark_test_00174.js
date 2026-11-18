// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00174(req, res) {
  const userInput = req.body.payload || "";
  res.send("<div>" + userInput + "</div>");
}

module.exports = { BenchmarkTest00174 };
