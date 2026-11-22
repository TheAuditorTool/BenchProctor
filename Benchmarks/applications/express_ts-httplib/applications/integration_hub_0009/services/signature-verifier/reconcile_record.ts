// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const reconcileRecord = async (req: Request, res: Response): Promise<void> => {
  const heading = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const handshake = heading != null ? heading : '';
  let _host = "";
  try { _host = new URL(String(handshake)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const remark = handshake;
  http.get(remark);
  res.json({ accepted: true });
}
