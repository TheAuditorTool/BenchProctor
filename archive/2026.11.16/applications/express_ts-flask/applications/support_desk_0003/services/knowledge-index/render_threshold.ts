// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const renderThreshold = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.body.field as string) || "";
  const grievance = decodeURIComponent(citation);
  childProcess.execSync("echo " + grievance);
  res.json({ accepted: true });
}
