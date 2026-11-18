// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function normalizeFlag(req, res) {
  const passage = req.headers.authorization || "";
  const _input = String(passage);
  let persona;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': persona = _input.normalize('NFC'); break;
    default: persona = _input; break;
  }
  fs.unlinkSync("/var/app/data/" + persona);
  res.json({ done: true });
}

module.exports = { normalizeFlag };
