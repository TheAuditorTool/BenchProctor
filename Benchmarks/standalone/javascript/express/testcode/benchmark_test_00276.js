// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const stream = require("node:stream");

async function BenchmarkTest00276(req, res) {
  const userInput = req.headers.authorization || "";
  const data = Buffer.from(userInput, "base64").toString();
  stream.Readable.from([String(data)]).pipe(crypto.createHash("md5")).setEncoding("hex").on("data", (checksum) => console.log("content checksum " + checksum));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00276 };
