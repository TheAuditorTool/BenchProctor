// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00218(req, res) {
  const userInput = req.params.id || "";
  const data = userInput != null ? userInput : '';
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00218 };
