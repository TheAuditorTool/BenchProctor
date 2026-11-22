// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const archiveWindow = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.body as string) || "";
  const backorder = await Promise.resolve(notice).then(String);
  const outbound = { method: "get", url: String(backorder), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
