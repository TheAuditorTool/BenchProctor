// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const rotateSchedule = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body.field as string) || "";
  const payload = { get value() { return remark; } };
  const synopsis = payload.value;
  net.connect(80, new URL(String(synopsis)).hostname);
  res.json({ accepted: true });
}
