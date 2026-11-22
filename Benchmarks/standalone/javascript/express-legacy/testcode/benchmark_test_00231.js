// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const stream = require("node:stream");

async function BenchmarkTest00231(req, res) {
  const userInput = req.body.payload || "";
  const data = `${userInput}`;
  stream.Readable.from([String(data)]).pipe(crypto.createHash("md5")).setEncoding("hex").on("data", (checksum) => console.log("content checksum " + checksum));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00231 };
