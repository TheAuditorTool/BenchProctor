// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const buildPolicy = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body as string) || "";
  const wording = String(footnote).split(/[ \t]+/).join(" ");
  http.get(wording);
  res.json({ accepted: true });
}
