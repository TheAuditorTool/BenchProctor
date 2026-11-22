// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as net from "net";

export const auditCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const memo = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const ledger = memo != null ? memo : '';
  let _host = "";
  try { _host = new URL(String(ledger)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const remittance = ledger;
  net.connect(80, new URL(String(remittance)).hostname);
  res.json({ accepted: true });
}
