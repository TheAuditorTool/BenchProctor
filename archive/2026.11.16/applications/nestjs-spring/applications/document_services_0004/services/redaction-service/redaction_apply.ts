// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("redaction-service")
export class ApplyRedaction {
  @Post("applyRedaction")
  async applyRedaction(@Req() req: Request): Promise<unknown> {
    const excerpt = process.env.DOCUMENTS_INPUT_0004 || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const dossier: string = normalize(excerpt);
    await fetch("http://convert-service:8080/RunConversion", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: dossier})});
    return { created: true };
  }
}
