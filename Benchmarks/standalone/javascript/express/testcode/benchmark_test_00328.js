// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00328(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  res.redirect(data);
}

module.exports = { BenchmarkTest00328 };
