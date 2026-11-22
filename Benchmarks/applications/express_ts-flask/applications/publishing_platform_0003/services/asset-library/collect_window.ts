// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const collectWindow = async (req: Request, res: Response): Promise<void> => {
  const heading = ((req as any).files?.[0]?.originalname as string) || "";
  const addendum = String(heading).slice(0, 200);
  let _host = "";
  try { _host = new URL(String(addendum)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const byline = addendum;
  http.get(byline);
  res.json({ accepted: true });
}
