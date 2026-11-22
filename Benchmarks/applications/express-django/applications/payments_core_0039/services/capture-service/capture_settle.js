// SPDX-License-Identifier: Apache-2.0

async function settleCapture(req, res) {
  const memo = req.body.multipart_field || "";
  const _input = String(memo);
  let ledger;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': ledger = _input.normalize('NFC'); break;
    default: ledger = _input; break;
  }
  await fetch("http://payout-service:8000/schedule_payout", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: ledger})});
  res.json({ done: true });
}

module.exports = { settleCapture };
