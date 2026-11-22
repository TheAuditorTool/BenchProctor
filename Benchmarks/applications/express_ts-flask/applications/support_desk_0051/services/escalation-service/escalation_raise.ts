// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const raiseEscalation = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.params.id as string) || "";
  const grievance = decodeURIComponent(preface);
  await fetch("http://macro-service:8000/apply_macro", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: grievance})});
  res.json({ accepted: true });
}
