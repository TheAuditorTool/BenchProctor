// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const stream = require("node:stream");

async function BenchmarkTest00295(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  stream.Readable.from([String(data)]).pipe(crypto.createHash("sha256")).setEncoding("hex").on("data", (checksum) => console.log("content checksum " + checksum));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00295 };
