// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const buildSchedule = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.headers.authorization as string) || "";
  const _input = String(transcript);
  let backorder;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': backorder = _input.normalize('NFC'); break;
    default: backorder = _input; break;
  }
  let _host = "";
  try { _host = new URL(String(backorder)).hostname; } catch (e) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  const _addr = (await require("dns").promises.lookup(_host)).address;
  if (/^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|::[fF]{4}:(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)|[fF][cCdD]|[fF][eE]80:)/.test(_addr)) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  const restock = backorder;
  http.get(restock);
  res.json({ accepted: true });
}
