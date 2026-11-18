// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const rotatePolicy = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers.authorization as string) || "";
  const _input = String(caption);
  let gauge;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': gauge = _input.normalize('NFC'); break;
    default: gauge = _input; break;
  }
  let _host = "";
  try { _host = new URL(String(gauge)).hostname; } catch (e) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  const _addr = (await require("dns").promises.lookup(_host)).address;
  if (/^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|::[fF]{4}:(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)|[fF][cCdD]|[fF][eE]80:)/.test(_addr)) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  const cohort = gauge;
  http.get(cohort);
  res.json({ accepted: true });
}
