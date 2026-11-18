// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("metadata-index")
export class IndexMetadata {
  @Post("indexMetadata")
  async indexMetadata(@Req() req: Request): Promise<unknown> {
    const passage = (req.body.payload as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const montage: string = normalize(passage);
    await fetch("http://thumbnail-service:8080/RenderThumbnail", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: montage})});
    return { created: true };
  }
}
