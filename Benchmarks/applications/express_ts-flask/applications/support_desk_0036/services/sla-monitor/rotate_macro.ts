// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const rotateMacro = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers.origin as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const grievance: string = normalize(preface);
  const inquiry = "/var/app/data/" + path.basename(grievance);
  const fileContent = fs.readFileSync(inquiry, "utf8");
  res.send(fileContent);
}
