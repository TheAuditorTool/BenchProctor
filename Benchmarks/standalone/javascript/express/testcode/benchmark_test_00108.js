// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00108(req, res) {
  const userInput = req.headers.host || "";
  const data = String(userInput).replace(/\u0000/g, "");
  return res.status(302).set("Location", String(data)).end();
}

module.exports = { BenchmarkTest00108 };
