// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function rotateSchedule(req, res) {
  const remark = req.headers.authorization || "";
  const _input = String(remark);
  let synopsis;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': synopsis = _input.normalize('NFC'); break;
    default: synopsis = _input; break;
  }
  fs.unlinkSync("/var/app/data/" + synopsis);
  res.json({ done: true });
}

module.exports = { rotateSchedule };
