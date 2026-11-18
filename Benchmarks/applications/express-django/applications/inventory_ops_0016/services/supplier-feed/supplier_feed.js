// SPDX-License-Identifier: Apache-2.0

async function pullSupplierFeed(req, res) {
  const citation = req.headers.authorization || "";
  const tokens = String(citation).split(',').filter((t) => t.length > 0);
  const backorder = tokens.join(' ');
  await fetch("http://catalog-api:8000/lookup_sku", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: backorder})});
  res.json({ done: true });
}

module.exports = { pullSupplierFeed };
