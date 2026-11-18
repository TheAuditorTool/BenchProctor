// SPDX-License-Identifier: Apache-2.0

async function convertFx(req, res) {
  const subject = (await require("./shared").mq.receive("app-events"));
  let ledger;
  try { ledger = JSON.parse(subject).value || ""; }
  catch (e) { ledger = String(subject); }
  await fetch("http://payments-api:8000/authorize_payment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: ledger})});
  res.json({ done: true });
}

module.exports = { convertFx };
