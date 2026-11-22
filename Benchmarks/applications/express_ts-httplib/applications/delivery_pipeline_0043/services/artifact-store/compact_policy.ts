// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const compactPolicy = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.params.id as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const note: string = normalize(remark);
  let _host = "";
  try { _host = new URL(String(note)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const phrase = note;
  net.connect(80, new URL(String(phrase)).hostname);
  res.json({ accepted: true });
}
