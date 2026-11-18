// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00536(req, res) {
  const userInput = req.headers.authorization || "";
  const data = Buffer.from(userInput, "hex").toString();
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00536 };
