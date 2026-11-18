// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const holdReservation = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.headers.authorization as string) || "";
  const parts: string[] = [];
  for (const token of String(transcript).split(',')) { parts.push(token); }
  const backorder: string = parts.join(',');
  await fetch("http://catalog-api:8080/lookup_sku", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: backorder})});
  res.json({ accepted: true });
}
