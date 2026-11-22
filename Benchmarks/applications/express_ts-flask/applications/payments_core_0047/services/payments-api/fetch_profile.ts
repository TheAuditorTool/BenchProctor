// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const fetchProfile = async (req: Request, res: Response): Promise<void> => {
  const footnote = ((req as any).files?.[0]?.originalname as string) || "";
  const remittance = String(footnote).slice(0, 200);
  let _host = "";
  try { _host = new URL(String(remittance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const disbursement = remittance;
  http.get(disbursement);
  res.json({ accepted: true });
}
