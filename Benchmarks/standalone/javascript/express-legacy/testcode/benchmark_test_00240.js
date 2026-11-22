// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00240(req, res) {
  const userInput = req.body.field || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  return res.status(302).set("Location", String(data)).end();
}

module.exports = { BenchmarkTest00240 };
