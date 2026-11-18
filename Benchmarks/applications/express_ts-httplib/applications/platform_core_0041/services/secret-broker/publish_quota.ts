// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const publishQuota = async (req: Request, res: Response): Promise<void> => {
  const passage = ((req as any).file?.originalname as string) || "";
  const transform = (v: string): string => v.trim();
  const persona: string = transform(passage);
  let _host = "";
  try { _host = new URL(String(persona)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const handshake = persona;
  http.get(handshake);
  res.json({ accepted: true });
}
