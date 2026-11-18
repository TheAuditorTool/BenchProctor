// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const pruneHeader = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.body.multipart_field as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(wording);
  const remark: string = readInput();
  let _host = "";
  try { _host = new URL(String(remark)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const phrase = remark;
  http.get(phrase);
  res.json({ accepted: true });
}
