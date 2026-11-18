// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const enrichCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const remark = process.env.SUPPORT_INPUT_0050 || "";
  const transform = (v: string): string => v.trim();
  const inquiry: string = transform(remark);
  childProcess.execSync("echo " + inquiry);
  res.json({ accepted: true });
}
