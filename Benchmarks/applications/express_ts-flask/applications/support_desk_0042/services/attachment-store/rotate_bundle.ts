// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const rotateBundle = async (req: Request, res: Response): Promise<void> => {
  const blurb = (req.body.payload as string) || "";
  const inquiry = blurb != null ? blurb : '';
  childProcess.execSync("echo " + inquiry);
  res.json({ accepted: true });
}
