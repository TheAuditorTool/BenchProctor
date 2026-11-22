// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("preview-renderer")
export class RenderPreview {
  @Post("renderPreview")
  async renderPreview(@Req() req: Request): Promise<unknown> {
    const snippet = req.body.publishing_payload || "";
    return "<div>" + snippet + "</div>";
  }
}
