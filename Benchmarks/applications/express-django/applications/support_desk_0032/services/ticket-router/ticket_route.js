// SPDX-License-Identifier: Apache-2.0

async function routeTicket(req, res) {
  const note = req.headers["x-custom-header"] || "";
  const tokens = String(note).split(',').filter((t) => t.length > 0);
  const inquiry = tokens.join(' ');
  await fetch("http://knowledge-index:8000/search_knowledge", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: inquiry})});
  res.json({ done: true });
}

module.exports = { routeTicket };
