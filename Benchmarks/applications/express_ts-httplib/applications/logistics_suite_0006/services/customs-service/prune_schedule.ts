// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const pruneSchedule = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body?.multipart_field as string) || "";
  const pending: string[] = String(summary).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const consignment: string = collected.join(',');
  const outbound = { method: "get", url: String(consignment), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
