// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00104(req, res) {
  const userInput = req.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00104 };
