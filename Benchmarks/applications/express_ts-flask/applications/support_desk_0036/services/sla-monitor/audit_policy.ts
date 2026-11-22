// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as net from "net";

export const auditPolicy = async (req: Request, res: Response): Promise<void> => {
  const preface = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const grievance = preface != null ? preface : '';
  let _host = "";
  try { _host = new URL(String(grievance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const inquiry = grievance;
  net.connect(80, new URL(String(inquiry)).hostname);
  res.json({ accepted: true });
}
