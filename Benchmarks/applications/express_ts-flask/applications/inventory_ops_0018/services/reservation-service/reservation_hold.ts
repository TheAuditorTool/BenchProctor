// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const holdReservation = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.body.payload as string) || "";
  const backorder = String(transcript).slice(0, 200);
  await fetch("http://catalog-api:8000/lookup_sku", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: backorder})});
  res.json({ accepted: true });
}
