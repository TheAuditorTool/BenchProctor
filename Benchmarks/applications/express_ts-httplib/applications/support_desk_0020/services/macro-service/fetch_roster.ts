// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const fetchRoster = async (req: Request, res: Response): Promise<void> => {
  const phrase = ((req as any).file?.originalname as string) || "";
  const transform = (v: string): string => v.trim();
  const inquiry: string = transform(phrase);
  let _host = "";
  try { _host = new URL(String(inquiry)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const grievance = inquiry;
  http.get(grievance);
  res.json({ accepted: true });
}
