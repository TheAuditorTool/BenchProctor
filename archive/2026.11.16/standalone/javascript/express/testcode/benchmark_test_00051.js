// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const crypto = require("crypto");

async function BenchmarkTest00051(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  const token = crypto.randomBytes(16).toString("hex");
  res.json({ token, label: String(data) });
}

module.exports = { BenchmarkTest00051 };
