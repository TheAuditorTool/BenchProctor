// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const loadConfig = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body.payload as string) || "";
  const byline = remark != null ? remark : '';
  childProcess.execSync("echo " + byline);
  res.json({ accepted: true });
}
