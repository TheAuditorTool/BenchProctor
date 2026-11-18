// SPDX-License-Identifier: Apache-2.0

async function lookupSku(req, res) {
  const phrase = req.query.id || "";
  const backorder = phrase != null ? phrase : '';
  await fetch("http://supplier-feed:8000/pull_supplier_feed", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: backorder})});
  res.json({ done: true });
}

module.exports = { lookupSku };
