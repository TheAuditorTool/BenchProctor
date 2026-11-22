// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const pruneCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.body as string) || "";
  const handshake = await Promise.resolve(wording).then(String);
  const outbound = { method: "get", url: String(handshake), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
