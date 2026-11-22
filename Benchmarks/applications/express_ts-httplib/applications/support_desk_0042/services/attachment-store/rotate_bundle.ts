// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const rotateBundle = async (req: Request, res: Response): Promise<void> => {
  const blurb = (req.body.field as string) || "";
  const inquiry = blurb != null ? blurb : '';
  childProcess.spawn("echo " + inquiry, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
