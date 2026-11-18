// SPDX-License-Identifier: Apache-2.0

async function fetchRoster(req, res) {
  const phrase = (await require("./shared").mq.receive("app-events"));
  let inquiry;
  try { inquiry = JSON.parse(phrase).value || ""; }
  catch (e) { inquiry = String(phrase); }
  JSON.parse(inquiry);
  res.json({ done: true });
}

module.exports = { fetchRoster };
