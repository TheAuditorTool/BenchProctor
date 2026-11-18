// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const summarizeBundle = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.body as string) || "";
  const persona = String(paragraph).split(/[ \t]+/).join(" ");
  http.get(persona);
  res.json({ accepted: true });
}
