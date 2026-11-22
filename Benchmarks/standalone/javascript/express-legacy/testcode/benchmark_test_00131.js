// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const stream = require("node:stream");

async function BenchmarkTest00131(req, res) {
  const userInput = req.body.field || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  stream.Readable.from([String(data)]).pipe(crypto.createHash("md5")).setEncoding("hex").on("data", (checksum) => console.log("content checksum " + checksum));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00131 };
