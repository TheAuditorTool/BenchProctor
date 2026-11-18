// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const mergeShipment = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body.field as string) || "";
  const parcel = decodeURIComponent(footnote);
  childProcess.execSync("echo " + parcel);
  res.json({ accepted: true });
}
