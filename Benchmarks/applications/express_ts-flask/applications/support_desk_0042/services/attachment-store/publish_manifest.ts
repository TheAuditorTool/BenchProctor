// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const publishManifest = async (req: Request, res: Response): Promise<void> => {
  const blurb = (req.params.id as string) || "";
  const inquiry = decodeURIComponent(blurb);
  if (!/^(asc|desc|name|created)$/.test(String(inquiry))) { res.status(400).json({error:"invalid"}); return; }
  const grievance = inquiry;
  childProcess.execSync("echo " + grievance);
  res.json({ accepted: true });
}
