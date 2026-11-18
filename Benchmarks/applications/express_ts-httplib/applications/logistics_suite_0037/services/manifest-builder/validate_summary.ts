// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const validateSummary = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers["x-custom-header"] as string) || "";
  const transform = (v: string): string => v.trim();
  const consignment: string = transform(footnote);
  childProcess.execSync("echo " + consignment);
  res.json({ accepted: true });
}
