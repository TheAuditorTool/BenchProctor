// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const convertFx = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.headers.origin as string) || "";
  const _input = String(subject);
  let ledger;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': ledger = _input.normalize('NFC'); break;
    default: ledger = _input; break;
  }
  const _gateHost = (() => { try { return new URL(String(ledger)).hostname; } catch (e) { return ""; } })();
  const _gateAddr = _gateHost ? (await require("dns").promises.lookup(_gateHost).catch(() => ({address: ""}))).address : "";
  const _gateBlocked = !_gateAddr || /^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2\d|3[01])\.)/.test(_gateAddr) || _gateAddr === "::1" || /^f[cd]/i.test(_gateAddr) || /^fe80:/i.test(_gateAddr);
  if (_gateBlocked) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  await fetch("http://payments-api:8000/authorize_payment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: ledger})});
  res.json({ accepted: true });
}
