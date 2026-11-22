// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const archiveReceipt = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers.host as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const cohort: string = normalize(note);
  const fileContent = fs.readFileSync("/var/app/data/" + cohort, "utf8");
  res.send(fileContent);
}
