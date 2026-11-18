// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00265(req, res) {
  const userInput = req.body.payload || "";
  const [data] = String(userInput).split(',');
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00265 };
