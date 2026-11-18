// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function loadSchedule(req, res) {
  const caption = req.headers.authorization || "";
  const _input = String(caption);
  let gauge;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': gauge = _input.normalize('NFC'); break;
    default: gauge = _input; break;
  }
  fs.unlinkSync("/var/app/data/" + gauge);
  res.json({ done: true });
}

module.exports = { loadSchedule };
