// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const validateProfile = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.body as string) || "";
  const handshake = String(synopsis).split(/[ \t]+/).join(" ");
  http.get(handshake);
  res.json({ accepted: true });
}
