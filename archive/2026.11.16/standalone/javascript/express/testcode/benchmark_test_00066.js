// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00066(req, res) {
  const userInput = (req.file && req.file.originalname) || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  req.session.data = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00066 };
