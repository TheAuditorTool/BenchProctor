// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const buildBundle = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers["x-custom-header"] as string) || "";
  const gauge = excerpt != null ? excerpt : '';
  http.get(gauge);
  res.json({ accepted: true });
}
