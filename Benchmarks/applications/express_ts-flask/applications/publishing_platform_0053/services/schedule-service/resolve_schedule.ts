// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const resolveSchedule = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers.referer as string) || "";
  const byline = decodeURIComponent(note);
  const outbound = { method: "get", url: String(byline), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
