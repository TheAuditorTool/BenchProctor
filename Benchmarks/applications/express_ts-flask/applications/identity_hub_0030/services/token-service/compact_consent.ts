// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const compactConsent = async (req: Request, res: Response): Promise<void> => {
  const tagline = ((req as any).files?.[0]?.originalname as string) || "";
  const persona = String(tagline).slice(0, 200);
  let _host = "";
  try { _host = new URL(String(persona)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const note = persona;
  http.get(note);
  res.json({ accepted: true });
}
