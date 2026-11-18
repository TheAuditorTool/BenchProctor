// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const rotateSnapshot = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body.multipart_field as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(summary);
  const restock: string = readInput();
  let _host = "";
  try { _host = new URL(String(restock)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const backorder = restock;
  http.get(backorder);
  res.json({ accepted: true });
}
