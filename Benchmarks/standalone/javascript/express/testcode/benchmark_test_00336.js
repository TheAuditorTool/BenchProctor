// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00336(req, res) {
  const userInput = req.query.id || "";
  const data = userInput != null ? userInput : '';
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00336 };
