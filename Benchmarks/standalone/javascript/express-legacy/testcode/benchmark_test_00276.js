// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const stream = require("node:stream");

async function BenchmarkTest00276(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  stream.Readable.from([String(data)]).pipe(crypto.createHash("md5")).setEncoding("hex").on("data", (checksum) => console.log("content checksum " + checksum));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00276 };
