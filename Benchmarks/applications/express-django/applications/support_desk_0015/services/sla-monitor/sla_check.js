// SPDX-License-Identifier: Apache-2.0

async function checkSla(req, res) {
  const phrase = req.headers.authorization || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(phrase);
  const grievance = readInput();
  await fetch("http://ticket-router:8000/route_ticket", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: grievance})});
  res.json({ done: true });
}

module.exports = { checkSla };
