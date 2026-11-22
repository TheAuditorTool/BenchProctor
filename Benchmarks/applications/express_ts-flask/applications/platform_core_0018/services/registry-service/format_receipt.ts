// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const formatReceipt = async (req: Request, res: Response): Promise<void> => {
  const subtitle = (req.headers.referer as string) || "";
  const persona = decodeURIComponent(subtitle);
  const outbound = { method: "get", url: String(persona), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
