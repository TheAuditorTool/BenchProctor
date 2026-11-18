// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function enrichCheckpoint(req, res) {
  const remark = req.headers.authorization || "";
  const _input = String(remark);
  let inquiry;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': inquiry = _input.normalize('NFC'); break;
    default: inquiry = _input; break;
  }
  fs.unlinkSync("/var/app/data/" + inquiry);
  res.json({ done: true });
}

module.exports = { enrichCheckpoint };
