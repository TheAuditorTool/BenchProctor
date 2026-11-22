// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const publishCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body.multipart_field as string) || "";
  const pending: string[] = String(remark).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const persona: string = collected.join(',');
  const outbound = { method: "get", url: String(persona), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
