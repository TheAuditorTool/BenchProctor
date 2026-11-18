// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function openDispute(req, res) {
  const subtitle = JSON.parse(fs.readFileSync("/etc/app/config.json", "utf8")).value;
  const _raw = subtitle;
  const ledger = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://payments-api:8000/authorize_payment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: ledger})});
  res.json({ done: true });
}

module.exports = { openDispute };
