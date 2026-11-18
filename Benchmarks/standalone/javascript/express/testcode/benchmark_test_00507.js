// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00507(req, res) {
  const userInput = req.cookies.session_token || "";
  const data = Buffer.from(userInput, "hex").toString();
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  res.json({ allocated: buf.length }); return;
}

module.exports = { BenchmarkTest00507 };
