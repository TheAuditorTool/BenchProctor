// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00056(req, res) {
  const userInput = req.body || "";
  const data = Buffer.from(userInput, "utf-8").toString();
  res.redirect(data);
}

module.exports = { BenchmarkTest00056 };
