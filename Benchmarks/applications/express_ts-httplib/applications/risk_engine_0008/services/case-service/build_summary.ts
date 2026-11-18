// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const buildSummary = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.headers["x-custom-header"] as string) || "";
  const _input = String(synopsis);
  let verdict;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': verdict = _input.normalize('NFC'); break;
    default: verdict = _input; break;
  }
  fs.writeFileSync("/var/uploads/" + verdict, "data");
  res.json({ accepted: true });
}
