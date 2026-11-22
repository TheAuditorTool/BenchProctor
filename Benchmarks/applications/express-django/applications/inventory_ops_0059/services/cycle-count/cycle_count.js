// SPDX-License-Identifier: Apache-2.0

async function runCycleCount(req, res) {
  const memo = req.headers["user-agent"] || "";
  const trim = (v) => String(v).trim();
  const backorder = trim(memo);
  await fetch("http://supplier-feed:8000/pull_supplier_feed", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: backorder})});
  res.json({ done: true });
}

module.exports = { runCycleCount };
