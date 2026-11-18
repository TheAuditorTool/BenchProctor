// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const validateReceipt = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers["x-custom-header"] as string) || "";
  const transform = (v: string): string => v.trim();
  const gauge: string = transform(summary);
  childProcess.execSync("echo " + gauge);
  res.json({ accepted: true });
}
