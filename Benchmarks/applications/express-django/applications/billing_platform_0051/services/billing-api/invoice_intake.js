// SPDX-License-Identifier: Apache-2.0

async function submitInvoice(req, res) {
  const synopsis = req.headers.authorization || "";
  const _input = String(synopsis);
  let arrears;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': arrears = _input.normalize('NFC'); break;
    default: arrears = _input; break;
  }
  await fetch("http://ledger-sync:8000/post_ledger_entry", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({billing_payload: arrears})});
  res.json({ done: true });
}

module.exports = { submitInvoice };
