// SPDX-License-Identifier: Apache-2.0

async function validateBundle(req, res) {
  const remark = (await require("./shared").mq.receive("app-events"));
  let synopsis;
  try { synopsis = JSON.parse(remark).value || ""; }
  catch (e) { synopsis = String(remark); }
  JSON.parse(synopsis);
  res.json({ done: true });
}

module.exports = { validateBundle };
