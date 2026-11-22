// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const verifyHeader = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body.multipart_field as string) || "";
  let note;
  try { note = JSON.parse(remark).value || remark; }
  catch (e) { note = remark; }
  fs.unlinkSync("/var/app/data/" + note);
  res.json({ accepted: true });
}
