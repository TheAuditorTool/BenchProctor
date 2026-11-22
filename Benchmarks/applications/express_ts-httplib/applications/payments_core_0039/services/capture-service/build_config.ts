// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const buildConfig = async (req: Request, res: Response): Promise<void> => {
  const memo = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const ledger = memo != null ? memo : '';
  let _host = "";
  try { _host = new URL(String(ledger)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const remittance = ledger;
  http.get(remittance);
  res.json({ accepted: true });
}
