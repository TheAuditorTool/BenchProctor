// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const compactCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.query.id as string) || "";
  const [backorder] = String(citation).split(',');
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(backorder)) { res.status(400).json({error:"invalid"}); return; }
  const restock = backorder;
  childProcess.execSync("echo " + restock);
  res.json({ accepted: true });
}
