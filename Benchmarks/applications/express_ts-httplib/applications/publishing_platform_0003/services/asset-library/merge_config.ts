// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const mergeConfig = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers.origin as string) || "";
  const _input = String(heading);
  let addendum;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': addendum = _input.normalize('NFC'); break;
    default: addendum = _input; break;
  }
  const fileContent = fs.readFileSync("/var/app/data/" + addendum, "utf8");
  res.send(fileContent);
}
