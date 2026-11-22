// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const compactThreshold = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.body.field as string) || "";
  const backorder = wording != null ? wording : '';
  childProcess.spawn("echo " + backorder, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
