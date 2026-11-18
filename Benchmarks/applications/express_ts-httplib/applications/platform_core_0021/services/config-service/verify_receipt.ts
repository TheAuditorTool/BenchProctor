// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const verifyReceipt = async (req: Request, res: Response): Promise<void> => {
  const excerpt = ((req as any).file?.originalname as string) || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(excerpt);
  let _host = "";
  try { _host = new URL(String(handshake)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const persona = handshake;
  http.get(persona);
  res.json({ accepted: true });
}
