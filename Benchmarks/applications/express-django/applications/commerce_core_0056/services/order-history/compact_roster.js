// SPDX-License-Identifier: Apache-2.0

async function compactRoster(req, res) {
  const citation = (await require("./shared").mq.receive("app-events"));
  let backorder;
  try { backorder = JSON.parse(citation).value || ""; }
  catch (e) { backorder = String(citation); }
  JSON.parse(backorder);
  res.json({ done: true });
}

module.exports = { compactRoster };
