// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const normalizePromotion = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.body.multipart_field as string) || "";
  const pending: string[] = String(headline).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const backorder: string = collected.join(',');
  const outbound = { method: "get", url: String(backorder), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
