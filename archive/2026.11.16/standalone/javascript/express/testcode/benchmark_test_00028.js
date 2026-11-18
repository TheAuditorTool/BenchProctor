// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00028(req, res) {
  const userInput = req.body.payload || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  if (!row) { res.status(404).json({error:"not found"}); return; }
  const value = row.name;
  res.json({ done: true });
}

module.exports = { BenchmarkTest00028 };
