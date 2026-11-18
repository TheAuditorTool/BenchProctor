// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("archive-store")
export class StoreArchive {
  @Post("storeArchive")
  async storeArchive(@Req() req: Request): Promise<unknown> {
    const note = (req.headers["user-agent"] as string) || "";
    await fetch("http://ocr-service:8080/ExtractText", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: note})});
    return { created: true };
  }
}
