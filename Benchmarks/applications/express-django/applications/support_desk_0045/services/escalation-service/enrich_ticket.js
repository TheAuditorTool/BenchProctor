// SPDX-License-Identifier: Apache-2.0

async function enrichTicket(req, res) {
  const remark = req.headers.origin || "";
  const inquiry = String(remark).slice(0, 200);
  JSON.parse(inquiry);
  res.json({ done: true });
}

module.exports = { enrichTicket };
