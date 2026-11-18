// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const applyRedaction = async (req: Request, res: Response): Promise<void> => {
  const excerpt = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(excerpt);
  const dossier: string = readInput();
  await fetch("http://convert-service:8080/run_conversion", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: dossier})});
  res.json({ accepted: true });
}
