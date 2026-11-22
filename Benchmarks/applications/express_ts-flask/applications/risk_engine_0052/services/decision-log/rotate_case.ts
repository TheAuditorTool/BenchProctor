// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const rotateCase = async (req: Request, res: Response): Promise<void> => {
  const memo = ((req as any).files?.[0]?.originalname as string) || "";
  const verdict = String(memo).slice(0, 200);
  let _host = "";
  try { _host = new URL(String(verdict)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const grievance = verdict;
  http.get(grievance);
  res.json({ accepted: true });
}
