// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const renderSnapshot = async (req: Request, res: Response): Promise<void> => {
  const blurb = (req.headers.host as string) || "";
  const handshake = `${blurb}`;
  let _host = "";
  try { _host = new URL(String(handshake)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const citation = handshake;
  http.get(citation);
  res.json({ accepted: true });
}
