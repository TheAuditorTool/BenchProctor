// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const publishWaybill = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.body.field as string) || "";
  const consignment = String(heading).slice(0, 200);
  JSON.parse(consignment);
  res.json({ accepted: true });
}
