// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const collectManifest = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.headers.host as string) || "";
  const handshake = `${synopsis}`;
  let _host = "";
  try { _host = new URL(String(handshake)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const memo = handshake;
  http.get(memo);
  res.json({ accepted: true });
}
