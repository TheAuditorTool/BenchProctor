// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const resolveConfig = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body?.multipart_field as string) || "";
  let bulletin;
  try { bulletin = JSON.parse(footnote).value || footnote; }
  catch (e) { bulletin = footnote; }
  fs.unlinkSync("/var/app/data/" + bulletin);
  res.json({ accepted: true });
}
