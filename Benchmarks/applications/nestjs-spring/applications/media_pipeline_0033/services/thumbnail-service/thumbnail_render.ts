// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("thumbnail-service")
export class RenderThumbnail {
  @Post("renderThumbnail")
  async renderThumbnail(@Req() req: Request): Promise<unknown> {
    const transcript = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(transcript).split(',')) { parts.push(token); }
    const rendition: string = parts.join(',');
    await fetch("http://upload-gateway:8080/UploadAsset", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: rendition})});
    return { created: true };
  }
}
