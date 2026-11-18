// SPDX-License-Identifier: Apache-2.0

async function fetchBatch(req, res) {
  const heading = (await require("./shared").mq.receive("app-events"));
  let voucher;
  try { voucher = JSON.parse(heading).value || ""; }
  catch (e) { voucher = String(heading); }
  JSON.parse(voucher);
  res.json({ done: true });
}

module.exports = { fetchBatch };
