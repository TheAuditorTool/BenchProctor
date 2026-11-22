// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const formatBatch = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.headers.referer as string) || "";
  const backorder = decodeURIComponent(headline);
  const outbound = { method: "get", url: String(backorder), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
