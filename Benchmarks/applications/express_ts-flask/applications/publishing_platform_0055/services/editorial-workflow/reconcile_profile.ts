// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const reconcileProfile = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.headers.host as string) || "";
  const byline = `${synopsis}`;
  http.get(byline);
  res.json({ accepted: true });
}
