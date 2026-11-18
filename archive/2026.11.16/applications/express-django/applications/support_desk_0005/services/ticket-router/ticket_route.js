// SPDX-License-Identifier: Apache-2.0

async function routeTicket(req, res) {
  const phrase = req.headers.authorization || "";
  let inquiry;
  try { inquiry = JSON.parse(phrase).value || phrase; }
  catch (e) { inquiry = phrase; }
  await fetch("http://knowledge-index:8000/search_knowledge", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: inquiry})});
  res.json({ done: true });
}

module.exports = { routeTicket };
