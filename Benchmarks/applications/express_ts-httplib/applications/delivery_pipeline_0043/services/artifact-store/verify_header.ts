// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const verifyHeader = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body?.multipart_field as string) || "";
  const pending: string[] = String(remark).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const note: string = collected.join(',');
  const outbound = { method: "get", url: String(note), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
