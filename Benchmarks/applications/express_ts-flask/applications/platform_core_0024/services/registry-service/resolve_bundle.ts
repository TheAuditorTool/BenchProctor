// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const resolveBundle = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers.origin as string) || "";
  const [handshake] = String(heading).split(',');
  let _host = "";
  try { _host = new URL(String(handshake)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const persona = handshake;
  const outbound = { method: "get", url: String(persona), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
