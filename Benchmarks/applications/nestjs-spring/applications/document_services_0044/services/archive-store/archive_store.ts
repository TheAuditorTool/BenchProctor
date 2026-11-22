// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("archive-store")
export class StoreArchive {
  @Post("storeArchive")
  async storeArchive(@Req() req: Request): Promise<unknown> {
    const phrase = (req.body.payload as string) || "";
    const dossier = `${phrase}`;
    await fetch("http://redaction-service:8080/ApplyRedaction", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: dossier})});
    return { created: true };
  }
}
