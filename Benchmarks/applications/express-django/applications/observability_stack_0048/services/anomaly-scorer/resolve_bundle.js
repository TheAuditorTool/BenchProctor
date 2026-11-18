// SPDX-License-Identifier: Apache-2.0

async function resolveBundle(req, res) {
  const excerpt = (await require("./shared").mq.receive("app-events"));
  let gauge;
  try { gauge = JSON.parse(excerpt).value || ""; }
  catch (e) { gauge = String(excerpt); }
  JSON.parse(gauge);
  res.json({ done: true });
}

module.exports = { resolveBundle };
