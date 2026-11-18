// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const verifySchedule = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.body.field as string) || "";
  const payload = { get value() { return notice; } };
  const persona = payload.value;
  net.connect(80, new URL(String(persona)).hostname);
  res.json({ accepted: true });
}
