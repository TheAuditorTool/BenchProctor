// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const routeTicket = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers["x-custom-header"] as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const inquiry: string = normalize(note);
  await fetch("http://knowledge-index:8000/search_knowledge", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: inquiry})});
  res.json({ accepted: true });
}
