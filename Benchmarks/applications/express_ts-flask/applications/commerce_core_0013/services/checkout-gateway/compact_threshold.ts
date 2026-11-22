// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const compactThreshold = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.headers.host as string) || "";
  const backorder = `${wording}`;
  http.get(backorder);
  res.json({ accepted: true });
}
