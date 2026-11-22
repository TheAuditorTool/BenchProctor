// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const rotateLedger = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.body.multipart_field as string) || "";
  let remittance;
  try { remittance = JSON.parse(caption).value || caption; }
  catch (e) { remittance = caption; }
  fs.unlinkSync("/var/app/data/" + remittance);
  res.json({ accepted: true });
}
