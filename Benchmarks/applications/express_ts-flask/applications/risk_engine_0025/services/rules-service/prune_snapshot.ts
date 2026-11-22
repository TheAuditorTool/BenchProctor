// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const pruneSnapshot = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers.origin as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const verdict: string = normalize(excerpt);
  const grievance = "/var/app/data/" + path.basename(verdict);
  const fileContent = fs.readFileSync(grievance, "utf8");
  res.send(fileContent);
}
