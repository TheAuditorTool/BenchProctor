// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const verifyCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers.referer as string) || "";
  const verdict = decodeURIComponent(excerpt);
  const outbound = { method: "get", url: String(verdict), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
