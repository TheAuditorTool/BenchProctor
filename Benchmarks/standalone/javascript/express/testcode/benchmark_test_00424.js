// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00424(req, res) {
  const userInput = req.headers.authorization || "";
  const data = Buffer.from(userInput, "hex").toString();
  res.redirect(data);
}

module.exports = { BenchmarkTest00424 };
