// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const rotateDigest = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers.origin as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const cohort: string = normalize(note);
  const gauge = "/var/app/data/" + path.basename(cohort);
  const fileContent = fs.readFileSync(gauge, "utf8");
  res.send(fileContent);
}
