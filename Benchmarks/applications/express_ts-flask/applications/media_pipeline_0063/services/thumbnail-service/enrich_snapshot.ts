// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const enrichSnapshot = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.params.id as string) || "";
  const montage = decodeURIComponent(snippet);
  if (!/^(asc|desc|name|created)$/.test(String(montage))) { res.status(400).json({error:"invalid"}); return; }
  const rendition = montage;
  childProcess.execSync("echo " + rendition);
  res.json({ accepted: true });
}
