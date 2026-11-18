// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const auditReport = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers.host as string) || "";
  const consignment = `${heading}`;
  http.get(consignment);
  res.json({ accepted: true });
}
