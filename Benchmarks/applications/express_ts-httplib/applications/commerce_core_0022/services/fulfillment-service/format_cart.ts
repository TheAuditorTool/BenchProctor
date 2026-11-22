// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const formatCart = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.params.id as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const voucher: string = normalize(subject);
  let _host = "";
  try { _host = new URL(String(voucher)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const backorder = voucher;
  net.connect(80, new URL(String(backorder)).hostname);
  res.json({ accepted: true });
}
