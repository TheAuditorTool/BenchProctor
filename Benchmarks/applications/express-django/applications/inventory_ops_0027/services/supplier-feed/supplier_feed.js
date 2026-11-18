// SPDX-License-Identifier: Apache-2.0

async function pullSupplierFeed(req, res) {
  const summary = req.headers["x-forwarded-for"] || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(summary);
  const restock = readInput();
  await fetch("http://allocation-service:8000/solve_allocation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: restock})});
  res.json({ done: true });
}

module.exports = { pullSupplierFeed };
