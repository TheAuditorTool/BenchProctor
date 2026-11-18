// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const summarizeConfig = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.headers.host as string) || "";
  const [grievance] = String(subject).split(',');
  net.connect(80, new URL(String(grievance)).hostname);
  res.json({ accepted: true });
}
