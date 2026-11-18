// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const loadConfig = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers["x-custom-header"] as string) || "";
  const transform = (v: string): string => v.trim();
  const grievance: string = transform(summary);
  childProcess.execSync("echo " + grievance);
  res.json({ accepted: true });
}
