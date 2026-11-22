// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");
const stream = require("node:stream");

async function BenchmarkTest00271(req, res) {
  const userInput = req.params.id || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  stream.Readable.from([String(data)]).pipe(crypto.createHash("sha256")).setEncoding("hex").on("data", (checksum) => console.log("content checksum " + checksum));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00271 };
