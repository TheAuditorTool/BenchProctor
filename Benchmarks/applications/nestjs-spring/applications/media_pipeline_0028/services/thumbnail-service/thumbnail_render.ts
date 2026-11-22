// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("thumbnail-service")
export class RenderThumbnail {
  @Post("renderThumbnail")
  async renderThumbnail(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(citation);
    const rendition: string = readInput();
    await fetch("http://metadata-index:8080/IndexMetadata", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: rendition})});
    return { created: true };
  }
}
