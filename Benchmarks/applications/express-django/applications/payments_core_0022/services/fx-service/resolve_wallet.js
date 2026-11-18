// SPDX-License-Identifier: Apache-2.0

async function resolveWallet(req, res) {
  const subject = req.body.payload || "";
  const _raw = subject;
  const ledger = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(ledger))) { res.status(400).json({error:"invalid"}); return; }
  const disbursement = ledger;
  res.send("<div>" + disbursement + "</div>");
}

module.exports = { resolveWallet };
