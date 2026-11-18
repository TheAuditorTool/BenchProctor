// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00363(req, res) {
  const userInput = req.headers.origin || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  res.redirect(data);
}

module.exports = { BenchmarkTest00363 };
