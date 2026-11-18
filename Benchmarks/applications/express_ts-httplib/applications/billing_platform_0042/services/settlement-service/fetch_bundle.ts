// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const fetchBundle = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers["x-custom-header"] as string) || "";
  const transform = (v: string): string => v.trim();
  const remittance: string = transform(remark);
  childProcess.execSync("echo " + remittance);
  res.json({ accepted: true });
}
