// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const compactIndex = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers.authorization as string) || "";
  const dossier = String(phrase).slice(0, 200);
  const outbound = { method: "get", url: String(dossier), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
