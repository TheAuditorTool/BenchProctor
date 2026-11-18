// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("watermark-service")
export class ApplyWatermark {
  @Post("applyWatermark")
  async applyWatermark(@Req() req: Request): Promise<unknown> {
    const tagline = (req.body as string) || "";
    const rendition = Buffer.from(tagline, "utf-8").toString();
    await fetch("http://metadata-index:8080/IndexMetadata", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: rendition})});
    return { created: true };
  }
}
