// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00217(req, res) {
  const userInput = req.headers.host || "";
  const data = userInput != null ? userInput : '';
  return res.status(302).set("Location", String(data)).end();
}

module.exports = { BenchmarkTest00217 };
