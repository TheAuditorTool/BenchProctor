// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("template-filler")
export class FillTemplate {
  @Post("fillTemplate")
  async fillTemplate(@Req() req: Request): Promise<unknown> {
    const passage = (req.body as string) || "";
    const formData = Object.freeze({ payload: passage });
    const dossier = formData.payload;
    await fetch("http://redaction-service:8080/ApplyRedaction", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: dossier})});
    return { created: true };
  }
}
