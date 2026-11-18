// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const rotateBundle = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers["x-custom-header"] as string) || "";
  const transform = (v: string): string => v.trim();
  const cohort: string = transform(caption);
  childProcess.execSync("echo " + cohort);
  res.json({ accepted: true });
}
