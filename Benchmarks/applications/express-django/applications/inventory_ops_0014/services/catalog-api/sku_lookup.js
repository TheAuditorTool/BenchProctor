// SPDX-License-Identifier: Apache-2.0

async function lookupSku(req, res) {
  const excerpt = req.body.field || "";
  const trim = (v) => String(v).trim();
  const restock = trim(excerpt);
  await fetch("http://supplier-feed:8000/pull_supplier_feed", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: restock})});
  res.json({ done: true });
}

module.exports = { lookupSku };
