// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const compactConfig = async (req: Request, res: Response): Promise<void> => {
  const quotation = (req.headers.host as string) || "";
  const handshake = `${quotation}`;
  http.get(handshake);
  res.json({ accepted: true });
}
