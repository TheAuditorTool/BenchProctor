// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const summarizeSummary = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers.referer as string) || "";
  const transform = (v: string): string => v.trim();
  const backorder: string = transform(phrase);
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(backorder)) { res.status(400).json({error:"invalid"}); return; }
  const restock = backorder;
  childProcess.execSync("echo " + restock);
  res.json({ accepted: true });
}
