// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const enrichWallet = async (req: Request, res: Response): Promise<void> => {
  const subtitle = (req.headers.host as string) || "";
  const ledger = `${subtitle}`;
  let _host = "";
  try { _host = new URL(String(ledger)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const remittance = ledger;
  http.get(remittance);
  res.json({ accepted: true });
}
