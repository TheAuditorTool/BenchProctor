// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const checkSla = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.params.id as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const grievance: string = normalize(phrase);
  await fetch("http://ticket-router:8080/route_ticket", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: grievance})});
  res.json({ accepted: true });
}
