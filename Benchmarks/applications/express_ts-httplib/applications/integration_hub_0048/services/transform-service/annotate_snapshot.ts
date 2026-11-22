// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const annotateSnapshot = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.body.multipart_field as string) || "";
  const pending: string[] = String(citation).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const handshake: string = collected.join(',');
  const outbound = { method: "get", url: String(handshake), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
