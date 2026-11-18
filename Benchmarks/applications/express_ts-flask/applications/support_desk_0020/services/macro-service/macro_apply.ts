// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const applyMacro = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.params.id as string) || "";
  const [inquiry] = String(phrase).split(',');
  await fetch("http://survey-service:8000/send_survey", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: inquiry})});
  res.json({ accepted: true });
}
