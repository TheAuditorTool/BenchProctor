// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const validateBatch = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.query.id as string) || "";
  const payload = { get value() { return summary; } };
  const handshake = payload.value;
  let _host = "";
  try { _host = new URL(String(handshake)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const paragraph = handshake;
  const outbound = { method: "get", url: String(paragraph), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
