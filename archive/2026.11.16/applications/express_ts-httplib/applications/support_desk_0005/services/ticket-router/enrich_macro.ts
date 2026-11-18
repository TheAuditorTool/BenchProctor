// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const enrichMacro = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const inquiry: string = normalize(phrase);
  fs.writeFileSync("/var/uploads/" + inquiry, "data");
  res.json({ accepted: true });
}
