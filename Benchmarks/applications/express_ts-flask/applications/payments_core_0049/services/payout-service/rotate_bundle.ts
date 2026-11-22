// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const rotateBundle = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.body.payload as string) || "";
  const disbursement = headline != null ? headline : '';
  childProcess.execSync("echo " + disbursement);
  res.json({ accepted: true });
}
