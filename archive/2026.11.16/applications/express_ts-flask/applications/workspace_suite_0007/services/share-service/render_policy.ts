// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const renderPolicy = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body.field as string) || "";
  const subtitle = decodeURIComponent(summary);
  childProcess.execSync("echo " + subtitle);
  res.json({ accepted: true });
}
