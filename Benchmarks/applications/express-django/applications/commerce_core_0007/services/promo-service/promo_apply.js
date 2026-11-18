// SPDX-License-Identifier: Apache-2.0

async function applyPromo(req, res) {
  const heading = req.query.id || "";
  const [voucher] = String(heading).split(',');
  await fetch("http://order-history:8000/lookup_order", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: voucher})});
  res.json({ done: true });
}

module.exports = { applyPromo };
