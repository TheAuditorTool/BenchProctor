// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const compactChannel = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body?.payload as string) || "";
  const bulletin = footnote != null ? footnote : '';
  childProcess.execSync("echo " + bulletin);
  res.json({ accepted: true });
}
